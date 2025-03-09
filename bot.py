
import random
from flask import Flask, jsonify
import requests

# Tvoj API ključ (ubaci tvoj stvarni ključ ovde)
API_KEY = '875c9d3a9f638bd1'  # Tvoj API ključ
XAT_API_URL = 'https://xat.com/web_gear/chat/'

# Lista imena i avatara
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

app = Flask(__name__)

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

# Web route za generisanje botova
@app.route('/generate_bots', methods=['GET'])
def generate_bots():
    botovi = []
    for i in range(25):
        bot_name = random.choice(imena_za_botove)
        bot_avatar = random.choice(avatare)
        postavi_bota(imena_za_botove, avatare)  # Postavi bota putem API-ja
        botovi.append({'name': bot_name, 'avatar': bot_avatar})
    
    return jsonify({"botovi": botovi})

# Pozdrav za goste
@app.route('/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Bot će pozdraviti nove korisnike kada se pridruže."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
