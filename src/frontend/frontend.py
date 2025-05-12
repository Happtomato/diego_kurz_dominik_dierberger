import streamlit as st
import json
import os
from datetime import datetime

SAVE_FILE = "/data/saved_recipes.json"

st.set_page_config(page_title="Gespeicherte Rezepte", layout="wide")
st.title("Gespeicherte Rezeptvorschläge")

if not os.path.exists(SAVE_FILE):
    st.warning("Noch keine Rezepte gespeichert.")
    st.stop()

with open(SAVE_FILE, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        st.error("Fehler beim Lesen der Rezeptdatei.")
        st.stop()
data.sort(key=lambda x: x["timestamp"], reverse=True)

for i, entry in enumerate(data):
    timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%d.%m.%Y %H:%M")
    ingredient_list = ", ".join(entry["ingredients"])

    with st.expander(f"{timestamp} – Zutaten: {ingredient_list}"):
        st.subheader("Rezeptvorschläge")

        for key, recipe in entry["recipes"].items():
            st.markdown(f"###{recipe['name']}")
            st.markdown(f"**Zutaten:** {', '.join(recipe['ingredients'])}")

            st.markdown("**Anleitung:**")
            if recipe.get("instructions"):
                for idx, step in enumerate(recipe["instructions"], start=1):
                    st.markdown(f"{idx}. {step}")
            else:
                st.warning("Keine Anleitung vorhanden.")