from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os
import time
import logging

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
RECIPE_ASSISTANT_ID = os.getenv("RECIPE_ASSISTANT_ID")
CONNECTAPIKEY = os.getenv("CONNECT_API_KEY")
# App setup
app = Flask(__name__)
CORS(app)

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def run_assistant_thread(message: str, assistant_id: str) -> str:
    """Run a message through an OpenAI Assistant thread and return the result."""
    thread = openai.beta.threads.create()
    logging.info(f"🧵 Thread created: {thread.id}")

    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    logging.info("💬 Message added to thread.")

    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )
    logging.info(f"🚀 Run started: {run.id}")

    # Poll for completion
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status in ("failed", "cancelled", "expired"):
            raise RuntimeError(f"Run failed with status: {run_status.status}")
        logging.info(f"⏳ Waiting... Current status: {run_status.status}")
        time.sleep(2)

    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value


@app.route("/suggest", methods=["POST"])
def suggest_recipe():
    """Suggest recipes based on a list of ingredients."""
    try:
        data = request.get_json()
        ingredients = data.get("ingredients", [])

        if not ingredients or not isinstance(ingredients, list):
            return jsonify({"error": "Please provide a list of ingredients"}), 400

        ingredient_string = ", ".join(ingredients)
        prompt = (
            f"Ich habe folgende Zutaten in meinem Kühlschrank: {ingredient_string}.\n"
            f"Bitte schlage mir drei kreative, einfache Rezepte vor, die ich damit kochen kann. "
            f"Gib sie nummeriert und in verständlicher Sprache zurück."
        )

        response = run_assistant_thread(prompt, RECIPE_ASSISTANT_ID)
        logging.info("✅ Rezeptvorschläge erhalten.")
        return jsonify({"rezepte": response}), 200

    except Exception as e:
        logging.error(f"❌ Fehler bei /suggest: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)