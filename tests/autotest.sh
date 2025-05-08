#!/bin/bash

echo "🔧 Starte automatisierte Checks..."

echo "📥 Installiere Python-Abhängigkeiten aus requirements.txt..."
pip install --quiet -r requirements.txt

echo "📦 TESTS mit pytest:"
pytest ../tests/ API_TEST.py

if [ $? -eq 0 ]; then
    echo "✅ Alle Checks erfolgreich!"
else
    echo "❌ Fehler bei Tests oder Linting."
    exit 1
fi