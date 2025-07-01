import fitz  # PyMuPDF
from pathlib import Path
import os
from dotenv import load_dotenv
import openai

# Charger les variables d'environnement
load_dotenv()

# Créer un client OpenAI (nouveau style SDK 1.x)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(text, model="gpt-3.5-turbo", max_tokens=1000):
    prompt = (
        "Résume le contenu scientifique suivant de façon claire et structurée :\n\n"
        f"{text[:3000]}"
    )

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Tu es un assistant expert en résumé d’articles scientifiques."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Erreur OpenAI :", e)
        return None

if __name__ == "__main__":
    pdf_path = "example.pdf"
    if not Path(pdf_path).exists():
        print(f"⚠️ Fichier {pdf_path} non trouvé.")
    else:
        full_text = extract_text_from_pdf(pdf_path)
        print("📄 PDF chargé. Envoi à OpenAI pour résumé...\n")
        summary = summarize_text(full_text)
        if summary:
            print("✅ Résumé généré :\n")
            print(summary)
