# BRF-system

Detta lilla projekt innehåller en Flask-applikation där medlemmar och styrelse kan logga in och se respektive information.

## Köra lokalt

1. Se till att Python 3 är installerat.
2. (Valfritt) skapa och aktivera ett virtuellt miljö:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Installera beroenden:
   ```bash
   pip install -r requirements.txt
   ```
4. Starta servern:
   ```bash
   python app.py
   ```
5. Öppna `http://localhost:5000` i din webbläsare.

Applikationen använder PrimeNG:s "saga-blue"-tema för en blå design.
