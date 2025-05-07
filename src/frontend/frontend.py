import streamlit as st
import json
import os
from datetime import datetime

SAVE_FILE = "saved_recipes.json"

st.set_page_config(page_title="Gespeicherte Rezepte", layout="wide")
st.title("📚 Gespeicherte Rezeptvorschläge")

if not os.path.exists(SAVE_FILE):
    st.warning("Noch keine Rezepte gespeichert.")
    st.stop()

with open(SAVE_FILE, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        st.error("❌ Fehler beim Lesen der Rezeptdatei.")
        st.stop()

# Sortierung nach Zeit (neueste oben)
data.sort(key=lambda x: x["timestamp"], reverse=True)

for i, entry in enumerate(data):
    timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%d.%m.%Y %H:%M")
    with st.expander(f"📅 {timestamp} – Zutaten: {', '.join(entry['ingredients'])}"):
        st.subheader("🍽️ Rezeptvorschläge")
        st.text(entry["recipes"])