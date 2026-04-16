import os
import sys
import time
import shutil
import threading
import psutil

# Próba importu biblioteki do obsługi GPU (NVIDIA)
try:
    import pynvml

    pynvml.nvmlInit()
    HAS_GPU = True
except Exception:
    HAS_GPU = False

# Próba importu biblioteki do wykresów
try:
    import matplotlib.pyplot as plt

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Ostrzeżenie: Biblioteka 'matplotlib' nie jest zainstalowana. Wykresy nie zostaną wygenerowane.")
    print("Zainstaluj ją wpisując: pip install matplotlib")

# Importujemy parsery z użyciem aliasów
from pdf_parser_pymupdf4llm import PdfParser as PyMuPdfParser
from pdf_parser_kreuzberg import PdfParser as KreuzbergParser
from pdf_parser_docling import PdfParser as DoclingParser
from pdf_parser_marker import PdfParser as MarkerParser
from pdf_parser_lmstudio import PdfParser as LmStudioParser
from pdf_parser_marker_llm import PdfParser as MarkerParserLlm
from pdf_parser_docling_llm import PdfParser as DoclingParserLlm


class ResourceMonitor:
    """Klasa do monitorowania zużycia RAM, CPU i GPU w osobnym wątku."""

    def __init__(self):
        self.keep_measuring = True
        self.cpu_measurements = []
        self.ram_measurements = []
        self.gpu_mem_measurements = []
        self.gpu_util_measurements = []
        self.thread = threading.Thread(target=self._measure)
        self.process = psutil.Process(os.getpid())

    def start(self):
        self.keep_measuring = True
        self.thread.start()

    def stop(self):
        self.keep_measuring = False
        self.thread.join()

    def _measure(self):
        self.process.cpu_percent(interval=None)

        while self.keep_measuring:
            cpu = self.process.cpu_percent(interval=None)
            self.cpu_measurements.append(cpu)

            ram_mb = self.process.memory_info().rss / (1024 * 1024)
            self.ram_measurements.append(ram_mb)

            if HAS_GPU:
                try:
                    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                    util_rate = pynvml.nvmlDeviceGetUtilizationRates(handle)
                    self.gpu_mem_measurements.append(mem_info.used / (1024 * 1024))
                    self.gpu_util_measurements.append(util_rate.gpu)
                except Exception:
                    pass

            time.sleep(0.1)

    def get_stats(self):
        stats = {
            "ram_peak_mb": max(self.ram_measurements) if self.ram_measurements else 0,
            "cpu_avg_percent": sum(self.cpu_measurements) / len(self.cpu_measurements) if self.cpu_measurements else 0,
            "cpu_peak_percent": max(self.cpu_measurements) if self.cpu_measurements else 0,
            "gpu_mem_peak_mb": max(self.gpu_mem_measurements) if self.gpu_mem_measurements else 0,
            "gpu_util_avg_percent": sum(self.gpu_util_measurements) / len(
                self.gpu_util_measurements) if self.gpu_util_measurements else 0
        }
        return stats


def run_parser_and_save(parser_name: str, parser_class, pdf_path: str, base_output_folder: str):
    output_folder = os.path.join(base_output_folder, parser_name)
    os.makedirs(output_folder, exist_ok=True)

    print(f"\n[{parser_name}] Przetwarzanie pliku: {pdf_path}...")

    parser = parser_class()
    monitor = ResourceMonitor()

    start_time = time.time()
    monitor.start()

    try:
        documents = parser.parse(pdf_path)
    except Exception as e:
        monitor.stop()
        raise e

    monitor.stop()
    end_time = time.time()

    elapsed_time = end_time - start_time
    resource_stats = monitor.get_stats()

    if not documents:
        print(f"[{parser_name}] Ostrzeżenie: Parsowanie zakończyło się pustym wynikiem.")
        return elapsed_time, 0, 0, resource_stats

    if not isinstance(documents, (list, tuple)):
        documents = [documents]

    base_name = os.path.basename(pdf_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    output_file_path = os.path.join(output_folder, f"{file_name_without_ext}.md")

    total_characters = 0

    print(f"[{parser_name}] Zapisywanie wyniku do: {output_file_path}")
    with open(output_file_path, "w", encoding="utf-8") as md_file:
        for doc in documents:
            page_num = doc.metadata.get("page_number", "?") if hasattr(doc, 'metadata') else "?"
            md_file.write(f"<!-- ELEMENT {page_num} -->\n")

            content = doc.page_content if hasattr(doc, 'page_content') else str(doc)
            total_characters += len(content)

            md_file.write(content)
            md_file.write("\n\n---\n\n")

    print(
        f"[{parser_name}] Gotowe! Zapisano elementów: {len(documents)}, Znaków: {total_characters}. Czas: {elapsed_time:.2f} s.")
    print(
        f"[{parser_name}] RAM (Peak): {resource_stats['ram_peak_mb']:.1f} MB | CPU (Avg): {resource_stats['cpu_avg_percent']:.1f}%")

    return elapsed_time, len(documents), total_characters, resource_stats


def generate_charts(timing_results, base_output_folder, file_name_without_ext):
    """Funkcja generująca obraz PNG z zestawieniem wyników na wykresach."""
    if not HAS_MATPLOTLIB or not timing_results:
        return

    # Przygotowanie danych
    parsers = [res['parser'] for res in timing_results]
    times = [res['time'] for res in timing_results]
    chars = [res['chars'] for res in timing_results]
    elements = [res['elements'] for res in timing_results]
    ram_peaks = [res['resources']['ram_peak_mb'] for res in timing_results]
    cpu_avgs = [res['resources']['cpu_avg_percent'] for res in timing_results]

    if HAS_GPU:
        gpu_peaks = [res['resources']['gpu_mem_peak_mb'] for res in timing_results]
    else:
        gpu_peaks = [0] * len(parsers)

    # Tworzenie siatki wykresów 2 wiersze x 3 kolumny
    fig, axs = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle(f'Benchmark Parserów PDF - Plik: {file_name_without_ext}', fontsize=16, fontweight='bold')

    # Funkcja pomocnicza do rysowania pojedynczego wykresu
    def plot_bar(ax, data, title, ylabel, color, is_int=False):
        bars = ax.bar(parsers, data, color=color, edgecolor='black')
        ax.set_title(title, fontsize=12)
        ax.set_ylabel(ylabel)
        ax.tick_params(axis='x', rotation=15)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Dodawanie wartości liczbowych nad słupkami
        for bar in bars:
            yval = bar.get_height()
            label = f'{int(yval)}' if is_int else f'{yval:.1f}'
            ax.text(bar.get_x() + bar.get_width() / 2, yval, label, ha='center', va='bottom', fontsize=10)

    # Wiersz 1
    plot_bar(axs[0, 0], times, 'Czas Wykonania (Mniej = Lepiej)', 'Sekundy', '#ff9999')
    plot_bar(axs[0, 1], ram_peaks, 'Maksymalne zużycie RAM (Mniej = Lepiej)', 'Megabajty (MB)', '#66b3ff')
    plot_bar(axs[0, 2], chars, 'Wyciągnięte Znaki (Wydajność Ekstrakcji)', 'Liczba Znaków', '#99ff99', is_int=True)

    # Wiersz 2
    plot_bar(axs[1, 0], cpu_avgs, 'Średnie zużycie CPU', 'Procent (%)', '#ffcc99')
    plot_bar(axs[1, 1], elements, 'Wyciągnięte Elementy (np. Strony)', 'Liczba', '#c2c2f0', is_int=True)

    if HAS_GPU:
        plot_bar(axs[1, 2], gpu_peaks, 'Maksymalne zużycie VRAM GPU', 'Megabajty (MB)', '#ffb3e6')
    else:
        axs[1, 2].text(0.5, 0.5, 'Brak danych GPU\n(Brak karty lub biblioteki)',
                       ha='center', va='center', fontsize=12, color='gray')
        axs[1, 2].set_title('Maksymalne zużycie VRAM GPU')
        axs[1, 2].axis('off')

    # Optymalizacja odstępów i zapis
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    chart_file_path = os.path.join(base_output_folder, f"charts_{file_name_without_ext}.png")
    plt.savefig(chart_file_path, dpi=150)
    plt.close()

    print(f"\n[Wykresy] Zapisano plik graficzny do: {chart_file_path}")


def process_pdf_to_test_folders(pdf_path: str):
    base_output_folder = "output"

    if os.path.exists(base_output_folder):
        print(f"Czyszczenie poprzednich wyników (usuwanie folderu '{base_output_folder}')...")
        shutil.rmtree(base_output_folder)

    os.makedirs(base_output_folder, exist_ok=True)

    if not os.path.exists(pdf_path):
        print(f"Błąd: Nie znaleziono pliku PDF pod ścieżką: {pdf_path}")
        return

    parsers = {
        "markerLlm": MarkerParserLlm,
        "doclingLlm": DoclingParserLlm,
        "llmstudio" : LmStudioParser,
        "pymupdf4llm": PyMuPdfParser,
        "kreuzberg": KreuzbergParser,
        "docling": DoclingParser,
        "marker" : MarkerParser
    }

    timing_results = []

    for name, p_class in parsers.items():
        try:
            elapsed_time, elements_count, total_chars, resource_stats = run_parser_and_save(
                name, p_class, pdf_path, base_output_folder
            )
            timing_results.append({
                "parser": name,
                "time": elapsed_time,
                "elements": elements_count,
                "chars": total_chars,
                "resources": resource_stats
            })
        except Exception as e:
            print(f"[{name}] Wystąpił błąd podczas przetwarzania: {e}")

    # Zapis raportu tekstowego
    base_name = os.path.basename(pdf_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    timing_file_path = os.path.join(base_output_folder, f"timing_{file_name_without_ext}.txt")

    print(f"\nZapisywanie raportu wydajnościowego do: {timing_file_path}")
    with open(timing_file_path, "w", encoding="utf-8") as t_file:
        t_file.write(f"Raport przetwarzania pliku: {pdf_path}\n")
        t_file.write(f"GPU Monitorowane: {'Tak' if HAS_GPU else 'Nie (Brak GPU NVIDIA lub biblioteki pynvml)'}\n")
        t_file.write("=" * 60 + "\n")

        for res in timing_results:
            r_stats = res["resources"]
            t_file.write(f"Parser: {res['parser']}\n")
            t_file.write(f"  Czas wykonania:          {res['time']:.4f} s\n")
            t_file.write(f"  Liczba elementów:        {res['elements']}\n")
            t_file.write(f"  Liczba znaków:           {res['chars']}\n")
            t_file.write(f"  RAM (Peak Process):      {r_stats['ram_peak_mb']:.2f} MB\n")
            t_file.write(f"  CPU (Avg Process):       {r_stats['cpu_avg_percent']:.2f} %\n")
            t_file.write(f"  CPU (Peak Process):      {r_stats['cpu_peak_percent']:.2f} %\n")

            if HAS_GPU:
                t_file.write(f"  GPU VRAM (Peak Total):   {r_stats['gpu_mem_peak_mb']:.2f} MB\n")
                t_file.write(f"  GPU Util (Avg Total):    {r_stats['gpu_util_avg_percent']:.2f} %\n")

            t_file.write("-" * 40 + "\n")

    # Generowanie i zapis wykresów (nowa funkcja)
    generate_charts(timing_results, base_output_folder, file_name_without_ext)

    print("\nZakończono wszystkie zadania pomyślnie. Sprawdź folder 'output'.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_pdf = sys.argv[1]
    else:
        target_pdf = "data/ISO_20022_Programme_UHB_SR2023_Edition-1-20.pdf"
        print(f"Nie podano pliku w argumencie. Używam domyślnego: {target_pdf}")

    process_pdf_to_test_folders(target_pdf)


# markitdown