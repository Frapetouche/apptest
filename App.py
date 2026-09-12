import streamlit as st, json, os
from datetime import date

# --- BIBLE VIVANTE PERSISTANTE ---
BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage yeux doux",
        "Bas-Rouge": "Beauceron noir et feu casque ailé viking torche foulard rouge yeux rouges furieux mais respectueux en hommage",
        "Mark Carney": "Golden Retriever premier ministre Canada cravate rouge drapeau Canada",
        "Monteur acier Kahnawake": "Husky casque chantier mohawk APTN",
        "Pompiers FDNY": "Bergers allemands casques FDNY courage",
        "Familles victimes": "Caniches blanc/beige/noir/marron bougies"
    }

def save_bible(bible):
    with open(BIBLE_FILE, "w", encoding="utf-8") as f:
        json.dump(bible, f, ensure_ascii=False, indent=2)

bible = load_bible()

# --- UI STREAMLIT ---
st.set_page_config(page_title="L'Extrémiste & Le Sage - Éditeur", layout="wide")
st.title("L'EXTRÉMISTE & LE SAGE — Éditeur Bible Vivante — Version Épurée")

# Sidebar = bible vivante qui s'agrandit
with st.sidebar:
    st.header("📖 Bible Vivante - Persos créés")
    st.write("Toujours ajouter à la bible vivante")
    for nom, desc in bible.items():
        st.text(f"{nom}: {desc}")
    
    new_nom = st.text_input("Ajouter nouveau perso")
    new_desc = st.text_input("Description chien 4 pattes")
    if st.button("Ajouter à bible"):
        bible[new_nom] = new_desc
        save_bible(bible)
        st.rerun()

# Main
sujet = st.text_input("Sujet du jour (ex: 25e anniversaire 11 sept - 2,977 drones 1 drone=1 vie)")
top = st.selectbox("TOP", ["TOP1", "TOP2", "TOP3", "TOP4", "TOP5"])
style = st.radio("Style", ["Version épurée moins de texte (70% moins)", "Version complète"], index=0)

if st.button("GÉNÉRER PROMPT FINAL POUR IMAGE"):
    prompt_final = f"""
L'EXTRÉMISTE & LE SAGE — NEWS DU JOUR {top} {date.today()} — {sujet}
9 cases 3x3 version épurée bible vivante 100% CHIENS À 4 PATTES AUCUN HUMAIN
TOUS CHIENS UNIQUES — BIBLE VIVANTE: {json.dumps(bible, ensure_ascii=False)}
STYLE: version épurée max 12 mots par case gros texte bold lisible parchemin Uderzo
CONSIGNES: sans répétition chaque chien unique 4 pattes casque ailé viking torche toujours Bas-Rouge
Case1: {sujet} 1 drone=1 vie si drone show 2,977 Lights Over New York Harbor
Case8: Bas-Rouge furieux ou respectueux selon hommage
Case9: Le Sage Labrador noir couronne + Bas-Rouge Beauceron dialogue mémoire prudence unité = solution
TITRE: L'EXTRÉMISTE & LE SAGE — {date.today()} — {sujet} — {top} — VERSION ÉPURÉE BIBLE VIVANTE 100% CHIENS VIVE MÉMOIRE!
"""
    st.code(prompt_final, language="text")
    st.download_button("Télécharger prompt", prompt_final, file_name="prompt_final.txt")

# Tableau persos disponibles pour prochaine fois
st.subheader("Tableau persos disponibles pour prochaine fois")
st.json(bible)
