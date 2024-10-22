from flask import Flask, request, jsonify

app = Flask(__name__)

# 存储聊天消息的列表 (示例)
messages = []

@app.route('/messages', methods=['GET'])
def get_messages():
    """返回所有消息的列表"""
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def post_message():
    """接收新消息并存储"""
    data = request.json
    if 'message' in data:
        message = data['message']
        messages.append(message)  # 将消息存储到列表中
        return jsonify({'status': 'success', 'message': message}), 201
    else:
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
