import requests
import random
import time

# Tvoj API ključ (ubaci tvoj stvarni ključ ovde)
API_KEY = '875c9d3a9f638bd1'  # Tvoj API ključ
XAT_API_URL = 'https://xat.com/web_gear/chat/'

# Lista imena i avataara
imena_za_botove = [
    "Ana", "Lana", "Maja", "Jelena", "Ivana", "Milena", "Sanja", "Katarina", "Marija", "Tina",
    "Petra", "Nina", "Ivona", "Mina", "Jovana", "Marko", "Nikola", "Vuk", "Luka", "Stefan",
    "David", "Filip", "Nemanja", "Andrej", "Bogdan", "Vladimir", "Aleksandar"
]

# Avatar linkovi (možeš zameniti sa svojim)
avatare = [
    "https://xat.com/web_gear/chat/avatars/1.png",
    "https://xat.com/web_gear/chat/avatars/2.png",
    "https://xat.com/web_gear/chat/avatars/3.png",
    # Dodaj više avatara po izboru
]

# Funkcija za postavljanje imena i avatara bota
def postavi_bota(imena, avatar):
    bot_name = random.choice(imena)  # Random ime za bota
    bot_avatar = random.choice(avatar)  # Random avatar za bota

    data = {
        'api_key': API_KEY,
        'name': bot_name,
        'avatar': bot_avatar,
    }

    response = requests.post(f"{XAT_API_URL}/setbot", data=data)
    if response.status_code == 200:
        print(f"Bot {bot_name} sa avatarom {bot_avatar} postavljen.")
    else:
        print("Greška prilikom postavljanja bota:", response.text)

# Pozdrav za nove korisnike
def pozdrav_za_goste():
    print("Bot će pozdraviti nove korisnike kada se pridruže.")
    # Ovo je samo simulacija, Xat API podržava automatsko slanje poruka kad neko uđe
    # Slično kao:
    # xat.chat.on('join', lambda user: xat.chat.send(f"Pozdrav {user.username}!"))

# Postavi 25 botova
for i in range(25):
    postavi_bota(imena_za_botove, avatare)
    time.sleep(1)  # Pauza između svakog bota

# Pozdrav za goste
pozdrav_za_goste()
