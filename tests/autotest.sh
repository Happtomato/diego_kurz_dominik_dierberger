#!/bin/bash

echo "Starte automatisierte Checks..."

exit_code = pytest.main(["API_Test.py"])

if [ $exit_code -eq 0 ]; then
    echo "✅ Alle Checks erfolgreich!"
else
    echo "❌ Fehler bei Tests oder Linting."
    exit 1
fi