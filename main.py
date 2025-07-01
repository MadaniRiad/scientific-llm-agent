# main.py

import fitz  # PyMuPDF
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_per_page = []
    for page in doc:
        text = page.get_text()
        text_per_page.append(text)
    return text_per_page

if __name__ == "__main__":
    pdf_path = "example.pdf"  # Remplace par le chemin de ton PDF
    if not Path(pdf_path).exists():
        print(f"Fichier {pdf_path} non trouvé.")
    else:
        pages = extract_text_from_pdf(pdf_path)
        for i, page_text in enumerate(pages[:2]):  # afficher les 2 premières pages
            print(f"--- Page {i+1} ---")
            print(page_text[:1000])  # les 1000 premiers caractères
            print("\n")

