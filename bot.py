from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Kreiranje bota
bot = ChatBot("ChatBot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

bots = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("add_bot")
def handle_add_bot(data):
    bot_id = data["id"]
    bots[bot_id] = {"name": data["name"], "color": data["color"]}
    emit("bot_added", data, broadcast=True)

@socketio.on("remove_bot")
def handle_remove_bot(bot_id):
    if bot_id in bots:
        del bots[bot_id]
        emit("bot_removed", bot_id, broadcast=True)

@socketio.on("update_bot")
def handle_update_bot(data):
    if data["id"] in bots:
        bots[data["id"]]["color"] = data["color"]
        emit("bot_updated", data, broadcast=True)

@socketio.on("user_message")
def handle_message(data):
    if data["bot_id"] in bots:
        response = bot.get_response(data["message"])
        emit("bot_response", {"bot_id": data["bot_id"], "message": str(response)}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

