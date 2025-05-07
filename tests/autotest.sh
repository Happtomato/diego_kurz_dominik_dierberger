#!/bin/bash

echo "🔧 Starte automatisierte Checks..."

echo "📦 TESTS mit pytest:"
pytest tests/
TEST_STATUS=$?

echo "🎨 FORMATIERUNG mit black:"
black src/ tests/ app.py api.py

echo "🧹 LINTING mit flake8:"
flake8 src/ tests/ app.py api.py
LINT_STATUS=$?

if [ $TEST_STATUS -eq 0 ] && [ $LINT_STATUS -eq 0 ]; then
    echo "✅ Alle Checks erfolgreich!"
    exit 0
else
    echo "❌ Fehler bei Tests oder Linting."
    exit 1
fi