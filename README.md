# Scientific LLM Agent

Un agent intelligent pour extraire et résumer automatiquement le contenu d’articles scientifiques au format PDF, en utilisant les modèles GPT d’OpenAI.

---

## Fonctionnalités

- Extraction du texte complet depuis un PDF scientifique.
- Résumé clair et structuré du contenu avec GPT-3.5-Turbo via l’API OpenAI.
- Code compatible avec la dernière version du SDK OpenAI (≥1.0.0).
- Facile à adapter pour d’autres fonctionnalités (questions de recherche, interface web...).

---

## Installation

### 1. Cloner le dépôt

```
git clone https://github.com/ton-utilisateur/scientific-llm-agent.git
cd scientific-llm-agent
```

### 2. Créer un environnement virtuel (recommandé)

Avec conda :
```
conda create -n llmagent python=3.11 -y
conda activate llmagent
```

### 3. Installer les dépendances
```
pip install -r requirements.txt
```

### 4. Configurer la clé API OpenAI

- Crée un fichier .env à la racine du projet

- Ajoute ta clé API OpenAI (remplace sk-xxx... par ta clé réelle)
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Usage
- Résumer un PDF
- Place ton fichier PDF dans le dossier du projet (exemple : example.pdf).
- Lance le script :
```
python main.py
```
Le script extrait le texte du PDF, puis envoie une requête à l’API OpenAI pour générer un résumé.

### Structure du projet
```
scientific-llm-agent/
├── main.py               # Script principal
├── requirements.txt      # Dépendances Python
├── .env                  # Variables d’environnement (clé API)
├── .gitignore            # Fichiers ignorés par git
└── README.md             # Documentation
```

### Prochaines étapes
- Ajouter la génération automatique de questions de recherche à partir du texte.

- Implémenter une interface web interactive avec Streamlit.

- Intégrer un modèle open source pour éviter la dépendance à OpenAI.

### Remarques

- Assurez-vous d’avoir un quota API actif chez OpenAI (voir https://platform.openai.com/account/usage)
- Le script traite uniquement les premiers 3000 caractères du texte extrait pour respecter les limites de tokens de l’API.

### Contact
Pour toute question ou suggestion, n’hésitez pas à ouvrir une issue ou me contacter via GitHub.
