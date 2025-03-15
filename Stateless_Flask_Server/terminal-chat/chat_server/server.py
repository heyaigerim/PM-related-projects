from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get JSON data from TerminalChat
    chat_message = data.get("chat", "")

    # Parsing the message based on assignment rules
    if chat_message.startswith("/"):
        parts = chat_message.split(" ", 1)
        command = parts[0][1:]  # Remove "/" from the command
        message = parts[1] if len(parts) > 1 else ""
    else:
        command = "None"
        message = chat_message

    response = {"chat": f"{command}: {message}"}
    return jsonify(response)

if __name__ == '__main__':
    # Running on port 5003 as specified
    app.run(host='0.0.0.0', port=5003, debug=True)
