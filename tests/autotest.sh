#!/bin/bash

echo "🔧 Starte automatisierte Checks..."

# 📦 Abhängigkeiten installieren
echo "📥 Installiere Python-Abhängigkeiten aus requirements.txt..."
pip install --quiet -r requirements.txt

# ✅ Tests
echo "📦 TESTS mit pytest:"
pytest ../tests/ API_TEST.py

# 🎨 Formatierung
echo "🎨 FORMATIERUNG mit black:"
black ../tests/ API_TEST.py

# 🧹 Linting
echo "🧹 LINTING mit flake8:"
flake8 ../tests/ API_TEST.py

# ✅ Erfolg oder Fehlerstatus
if [ $? -eq 0 ]; then
    echo "✅ Alle Checks erfolgreich!"
else
    echo "❌ Fehler bei Tests oder Linting."
    exit 1
fi