from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# 存储聊天消息的列表 (示例)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    messages.append(message)  # 将消息存储到列表中
    emit('receive_message', {'message': message}, broadcast=True)

@socketio.on('get_messages')
def handle_get_messages():
    emit('receive_message', {'messages': messages})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, use_reloader=True)
