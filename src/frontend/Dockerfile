# Basis-Image mit Python 3.10.6
FROM python:3.10.6-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Abhängigkeiten kopieren
COPY requirements.txt .

# Abhängigkeiten installieren
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Streamlit-Port freigeben
EXPOSE 8501

# Startbefehl (wird von docker-compose überschrieben, ist hier aber korrekt als fallback)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]