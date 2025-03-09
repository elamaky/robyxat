import requests
from bs4 import BeautifulSoup
import random
import time

# Tvoj API ključ
API_KEY = '1014faacbd7a10ce'  # Zameniti sa tvojim stvarnim ključem
XAT_API_URL = 'https://xat.com/web_gear/chat/setbot'  # Xat API endpoint

# Funkcija za preuzimanje podataka iz HTML fajla
def preuzmi_botove_iz_html():
    with open('botovi.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

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
    data = {
        'api_key': API_KEY,  # Tvoj API ključ
        'name': bot['ime'],
        'avatar': bot['avatar'],
        # 'message': bot['poruka'],  # Opcionalno ako Xat API podržava slanje poruka
    }

    response = requests.post(XAT_API_URL, data=data)

    if response.status_code == 200:
        print(f"Bot {bot['ime']} sa avatarom {bot['avatar']} postavljen.")
    else:
        print(f"Greška prilikom postavljanja bota: {response.text}")

# Preuzimamo podatke o botovima iz HTML fajla
botovi = preuzmi_botove_iz_html()

# Postavljamo botove
for bot in botovi:
    postavi_bota(bot)
    time.sleep(1)  # Pauza između svakog bota
