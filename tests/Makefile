# Installiere alle Abhängigkeiten aus requirements.txt
install:
	pip install -r requirements.txt

# Führe alle Tests im Verzeichnis tests/ aus
test:
	pytest tests/

# Optional: Formatierung mit black (falls installiert)
format:
	black src/ tests/ app.py api.py

# Optional: Linting mit flake8
lint:
	flake8 src/ tests/ app.py api.py

# Kombinierter Test- und Qualitätscheck
check: test lint format