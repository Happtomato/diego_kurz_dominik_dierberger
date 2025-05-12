# IAI Project – Diego Kurz and Dominik Dierberger

_This is the IAI Project of Diego Kurz and Dominik Dierberger in the module "Introduction to AI" in the spring semester of 2025._

This project is a recipe book where you can input ingredients and with the help of ChatGPT it will provide you with a recipe.  
Recipes can be saved to a recipe book to be looked at again at a later stage.  
You can use the tool either via command line or via a web-based frontend.

---

## Setup Instructions

To set up this project please [download](link) the project as a zip file from GitLab.

Once the zip file is downloaded you can open it in an IDE of your choosing.

Open the file `.env` (or create it) and replace the API key for OpenAI with your own.  
You can get an API key [here](https://platform.openai.com/account/api-keys).

Example content of `.env`:

```

OPENAI_API_KEY=your_api_key_here
RECIPE_ASSISTANT_ID=optional_assistant_id

````

Make sure you have Docker and Docker Compose installed. All dependencies are managed via Docker.

---

## How to Run the Project

Once your setup is complete, you can run the project by starting Docker Compose:

```bash
docker-compose up --build
````

To **create new recipes**, you need to run the CLI manually (either inside the container or from a local Python environment):

```bash
python main.py --ingredients "bananas, eggs, milk, strawberries"
```

* You will be prompted to enter ingredients.
* A request will be sent to ChatGPT, which returns a recipe suggestion.
* You can then choose whether or not to save the recipe.

Saved recipes are stored in a file called `saved_recipes.json`.

You can view your saved recipes in two ways:

* The **Streamlit web interface** at: [http://localhost:8501](http://localhost:8501)
* The **Jupyter Notebook** `Rezeptbuch.ipynb` as a digital recipe collection

In the web interface, recipes are displayed in two forms:

* **Raw JSON** with timestamp and ingredients
* **Formatted recipe suggestions** in collapsible sections

---

## Example Commands and Explanations

> Example of choosing ingredients for your recipe

**Expected prompt:** Please input the ingredients you want to use for your recipe
**Possible user input:** Bananas, Eggs, Milk, Strawberries

ChatGPT will provide a recipe using the ingredients entered by the user.

> Prompt if you want to save the recipe or not

**Expected prompt:** Do you want to save this recipe to your recipe book?
**User input:** y or n

Depending on user choice, the recipe will be saved (y) or not saved (n) to the recipe book.

---

## Expected Outputs

**Example input:** Bananas, Eggs, Milk, Strawberries
**Expected output:** A recipe for pancakes, for example, with instructions

The recipe is printed to the terminal and (if chosen) saved in `saved_recipes.json`.

The saved JSON file will contain e.G.:

```json
[
  {
    "timestamp": "2025-05-07T10:26:52.762407",
    "ingredients": [
      "sahne",
      "eier",
      "pasta"
    ],
    "recipes": {
      "recipe1": {
        "name": "Cremige Eiernudeln",
        "ingredients": [
          "Pasta",
          "Eier",
          "Sahne",
          "Salz",
          "Pfeffer",
          "Knoblauch",
          "Parmesan"
        ],
        "instructions": [
          "Die Pasta nach Packungsanweisung in einem Topf mit Salzwasser al dente kochen und abgießen.",
          "In einer Schüssel die Eier mit der Sahne, Salz, Pfeffer und gehacktem Knoblauch verquirlen.",
          "Die heiße Pasta zurück in den Topf geben und vom Herd nehmen.",
          "Die Eier-Sahne-Mischung über die heiße Pasta gießen und gut umrühren, sodass die Eier leicht stocken und eine cremige Sauce entsteht.",
          "Den geriebenen Parmesan hinzufügen und erneut umrühren.",
          "Warm servieren und nach Belieben mit frischen Kräutern garnieren."
        ]
      },
      "recipe2": {
        "name": "Pasta Frittata",
        "ingredients": [
          "Pasta",
          "Eier",
          "Sahne",
          "Salz",
          "Pfeffer",
          "Olivenöl",
          "Zwiebel"
        ],
        "instructions": [
          "Die Pasta vom Vortag verwenden oder frisch kochen und abkühlen lassen.",
          "Die Eier in einer Schüssel mit Sahne, Salz und Pfeffer verquirlen.",
          "Eine Pfanne mit Olivenöl erhitzen und die gehackte Zwiebel darin anbraten, bis sie glasig ist.",
          "Die gekochte Pasta in die Pfanne hinzufügen und kurz durchrühren.",
          "Die Eiermischung darüber gießen und bei mittlerer Hitze stocken lassen.",
          "Wenn die Ränder fest werden, die Pfanne in den vorgeheizten Ofen schieben und bei 180 Grad Celsius ca. 10 Minuten backen, bis die Frittata komplett gestockt und leicht gebräunt ist.",
          "Warm oder kalt servieren."
        ]
      },
      "recipe3": {
        "name": "Sahne-Eierauflauf mit Pasta",
        "ingredients": [
          "Pasta",
          "Eier",
          "Sahne",
          "Salz",
          "Pfeffer",
          "Muskatnuss",
          "Butter"
        ],
        "instructions": [
          "Die Pasta al dente kochen und abgießen.",
          "Den Backofen auf 180 Grad Celsius vorheizen.",
          "Eine Auflaufform mit Butter ausstreichen.",
          "In einer Schüssel die Eier mit der Sahne, Salz, Pfeffer und einer Prise Muskatnuss verquirlen.",
          "Die gekochte Pasta in die vorbereitete Auflaufform geben und die Eier-Sahne-Mischung darüber gießen.",
          "Eventuell nochmals mit Salz und Pfeffer abschmecken.",
          "Im Ofen ca. 20-25 Minuten backen, bis die Oberfläche goldbraun ist und der Auflauf durchgestockt ist.",
          "Heiß servieren."
        ]
      }
    }
  },
  ...
]
```

The web frontend will display this in a clean, structured format for easier browsing.

---

## Dependencies and Environment

All dependencies and environments will be set up automatically when the project is run for the first time using Docker Compose.

Alternatively, if running locally:

```bash
pip install -r requirements.txt
```

Dependencies include:

* Python 3.10
* Flask
* Streamlit
* OpenAI Python SDK
* python-dotenv
* requests
* pytest

The project uses environment variables for API keys. These are stored in a `.env` file, which is excluded from Git tracking via `.gitignore`.

---

## Credits

* **Group Members:** Diego Kurz, Dominik Dierberger
* **External Resources:**

  * [OpenAI assistant services](https://platform.openai.com/docs/assistants/overview)
  * Streamlit
  * Flask
  * Python Dotenv
