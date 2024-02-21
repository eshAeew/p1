from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

chat_history = []

@socketio.on('message')
def handle_message(data):
    chat_history.append(data)
    send(data, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    socketio.run(app)
