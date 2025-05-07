import requests
import json
import os
from datetime import datetime

API_URL = "http://localhost:5050/suggest"
SAVE_FILE = "saved_recipes.json"

def call_recipe_api(ingredients):
    try:
        response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"ingredients": ingredients})
        )
        if response.status_code == 200:
            return response.json()["rezepte"]
        else:
            print(f"❌ Fehler {response.status_code}: {response.json().get('error')}")
    except Exception as e:
        print(f"❌ Anfrage fehlgeschlagen: {e}")
    return None

def prompt_save(ingredients, recipes_text):
    print("\n💾 Möchtest du das Ergebnis speichern? (j/n)")
    choice = input(">> ").strip().lower()
    if choice == "j":
        save_data(ingredients, recipes_text)
    else:
        print("📭 Nicht gespeichert.")

def save_data(ingredients, recipes_text):
    recipe_entry = {
        "timestamp": datetime.now().isoformat(),
        "ingredients": ingredients,
        "recipes": recipes_text
    }

    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(recipe_entry)

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Rezept gespeichert in '{SAVE_FILE}'.")

def main():
    print("👩‍🍳 Willkommen beim Rezeptfinder!")
    input_string = input("🧺 Gib deine Zutaten ein (kommagetrennt, z. B. 'tomaten,eier,käse'):\n>> ")
    ingredients_list = [x.strip() for x in input_string.split(",") if x.strip()]

    if not ingredients_list:
        print("⚠️ Keine gültigen Zutaten eingegeben.")
        return

    print("📡 Rezept wird angefragt...")
    recipes_text = call_recipe_api(ingredients_list)

    if recipes_text:
        print("\n🍽️  Rezeptvorschläge:\n")
        print(recipes_text)
        prompt_save(ingredients_list, recipes_text)

if __name__ == "__main__":
    main()