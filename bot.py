from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Memorija za čuvanje trenutnih botova (dok traje sesija)
bots = {}

# Ruta za glavnu stranicu - učitaj HTML iz templates foldera
@app.route('/')
def index():
    return render_template("index.html")  # Vraća index.html iz templates foldera

# Događaj za dodavanje bota
@socketio.on("add_bot")
def handle_add_bot(data):
    bot_id = data["id"]
    bots[bot_id] = {"name": data["name"], "color": data["color"]}
    print(f"Bot added: {bots[bot_id]}")
    emit("bot_added", data, broadcast=True)

# Događaj za uklanjanje bota
@socketio.on("remove_bot")
def handle_remove_bot(bot_id):
    if bot_id in bots:
        del bots[bot_id]
        print(f"Bot removed: {bot_id}")
        emit("bot_removed", bot_id, broadcast=True)

# Pokretanje servera
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
