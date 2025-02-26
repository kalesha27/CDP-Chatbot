from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses for 'How-to' questions
responses = {
    "how to reset password": "To reset your password, go to the settings page and click 'Reset Password'.",
    "how to create account": "Visit our website, click 'Sign Up', and fill in your details."
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").lower()
    response = responses.get(user_input, "I'm sorry, I don't have an answer for that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
