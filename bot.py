from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Xat API ključ (zameni sa stvarnim API ključem)
API_KEY = '875c9d3a9f638bd1'  # Tvoj stvarni API ključ

# Lista botova sa imenom, avatarom i porukom
botovi = [
    {"ime": "Ana", "avatar": "https://xat.com/web_gear/chat/avatars/1.png", "poruka": "Pozdrav!"},
    {"ime": "Marko", "avatar": "https://xat.com/web_gear/chat/avatars/2.png", "poruka": "Dobrodošao!"}
]

# Ruta za početnu stranicu
@app.route('/')
def home():
    return render_template('index.html', botovi=botovi)

# Ruta za dodavanje novog bota
@app.route('/add_bot', methods=['POST'])
def add_bot():
    ime = request.form['ime']
    avatar = request.form['avatar']
    poruka = request.form['poruka']
    botovi.append({"ime": ime, "avatar": avatar, "poruka": poruka})

    # Pozivanje Xat API-ja da pošalje poruku
    posalji_poruku_na_xat(ime, poruka)

    return render_template('index.html', botovi=botovi)

# Funkcija za slanje poruke na Xat chat
def posalji_poruku_na_xat(bot_ime, poruka):
    url = "https://xat.com/web_gear/chat/send_message.php"
    params = {
        "api_key": API_KEY,  # Tvoj API ključ
        "bot_name": bot_ime,
        "message": poruka
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print(f"Poruka od {bot_ime}: '{poruka}' je poslana.")
    else:
        print(f"Greška pri slanju poruke: {response.text}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
