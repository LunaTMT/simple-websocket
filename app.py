from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Sample chat history
chat_history = []

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    # Send chat history to the connected client
    emit('chat_history', chat_history)

@socketio.on('message')
def handle_message(data):
    # Handle incoming messages
    # You can save new messages to chat_history and broadcast them to other clients
    chat_history.append(data)
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
