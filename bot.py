import requests
import random
import time

# Tvoj API ključ
API_KEY = '1014faacbd7a10ce'  # Zameniti sa tvojim stvarnim ključem
XAT_API_URL = 'https://xat.com/web_gear/chat/setbot'  # Xat API endpoint

# Lista imena i avataara
imena_za_botove = [
    "Ana", "Lana", "Maja", "Jelena", "Ivana", "Milena", "Sanja", "Katarina", "Marija", "Tina",
    "Petra", "Nina", "Ivona", "Mina", "Jovana", "Marko", "Nikola", "Vuk", "Luka", "Stefan",
    "David", "Filip", "Nemanja", "Andrej", "Bogdan", "Vladimir", "Aleksandar"
]

# Avatar linkovi
avatare = [
    "https://xat.com/web_gear/chat/avatars/1.png",
    "https://xat.com/web_gear/chat/avatars/2.png",
    "https://xat.com/web_gear/chat/avatars/3.png",
    # Dodaj više avatara po izboru
]

# Funkcija za postavljanje bota
def postavi_bota(imena, avatar):
    bot_name = random.choice(imena)  # Random ime za bota
    bot_avatar = random.choice(avatar)  # Random avatar za bota

    data = {
        'api_key': API_KEY,  # Tvoj API ključ
        'name': bot_name,
        'avatar': bot_avatar,
    }

    response = requests.post(XAT_API_URL, data=data)

    if response.status_code == 200:
        print(f"Bot {bot_name} sa avatarom {bot_avatar} postavljen.")
    else:
        print(f"Greška prilikom postavljanja bota: {response.text}")

# Kreiraj botove
for i in range(25):  # Postavi 25 botova
    postavi_bota(imena_za_botove, avatare)
    time.sleep(1)  # Pauza između svakog bota
