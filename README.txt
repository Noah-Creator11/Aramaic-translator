
ARAMÄISCH-ÜBERSETZER – INSTALLATION

1. Voraussetzungen:
- Python 3.x installiert
- OpenAI API-Schlüssel (https://platform.openai.com/account/api-keys)

2. Installation:
Öffne ein Terminal und führe aus:

python -m venv venv
# Dann aktivieren:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Dann:
pip install flask openai

3. API-Schlüssel einfügen:
Öffne 'server.py' und ersetze DEIN_API_KEY durch deinen echten OpenAI API Key.

4. Server starten:
python server.py

5. index.html öffnen:
Doppelklick auf index.html und den Button „Übersetzen“ testen.
