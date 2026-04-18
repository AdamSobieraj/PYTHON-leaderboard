# debug_pdf_images.py
# Uruchom: python debug_pdf_images.py

import fitz  # PyMuPDF

PDF_PATH = "data/ISO_20022_Programme_UHB_SR2023_Edition-1-20.pdf"

pdf = fitz.open(PDF_PATH)

total_images = 0

for i, page in enumerate(pdf):
    images = page.get_images(full=True)
    text_blocks = page.get_text("blocks")

    print(f"Strona {i + 1}: obrazów={len(images)}, bloków tekstu={len(text_blocks)}")

    for img in images:
        xref = img[0]
        print(f"  → Obraz xref={xref}, rozmiar={pdf.extract_image(xref)['width']}x{pdf.extract_image(xref)['height']}")
        total_images += 1

pdf.close()
print(f"\nŁącznie obrazów w całym PDF: {total_images}")