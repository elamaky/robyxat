import requests
from bs4 import BeautifulSoup
import time
import os

# Tvoj API ključ
API_KEY = '1014faacbd7a10ce'  # Zameniti sa tvojim stvarnim ključem
XAT_API_URL = 'https://xat.com/web_gear/chat/setbot'  # Xat API endpoint
CHAT_NAME = "RadioProkuplje"  # Promeni na svoj chat

# Funkcija za dobijanje Chat ID-a
def dohvati_chat_id(chat_ime):
    response = requests.get(f"https://xat.com/web_gear/chat/roomid.php?d={chat_ime}")
    if response.status_code == 200 and response.text.isdigit():
        return response.text.strip()
    else:
        print("Greška prilikom dobijanja Chat ID-a:", response.text)
        return None

# Dobijanje Chat ID-a
CHAT_ID = dohvati_chat_id(CHAT_NAME)

# Funkcija za preuzimanje podataka iz HTML fajla
def preuzmi_botove_iz_html():
    # Ako je fajl "index.html", pročitaj ga
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
    else:
        print("Fajl 'index.html' nije pronađen.")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    botovi = []

    # Preuzimamo podatke iz tabele
    for row in soup.find_all('tr')[1:]:  # Preskočimo prvi red (zaglavlje)
        columns = row.find_all('td')
        ime = columns[0].text.strip()
        avatar = columns[1].text.strip()
        poruka = columns[2].text.strip()
        botovi.append({'ime': ime, 'avatar': avatar, 'poruka': poruka})

    return botovi

# Funkcija za postavljanje bota
def postavi_bota(bot):
    if not CHAT_ID:
        print("Neuspešno dobijanje Chat ID-a. Bot se ne može postaviti.")
        return

    data = {
        'api_key': API_KEY,
        'name': bot['ime'],
        'avatar': bot['avatar'],
        'roomid': CHAT_ID,  # Dodajemo Chat ID
    }

    response = requests.post(XAT_API_URL, data=data)

    if response.status_code == 200:
        print(f"Bot {bot['ime']} postavljen u chat {CHAT_NAME}.")
    else:
        print(f"Greška prilikom postavljanja bota: {response.text}")

# Preuzimamo podatke o botovima iz HTML fajla
botovi = preuzmi_botove_iz_html()

# Postavljamo botove
for bot in botovi:
    postavi_bota(bot)
    time.sleep(1)  # Pauza između svakog bota
