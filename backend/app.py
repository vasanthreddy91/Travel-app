from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if data['username'] == "admin" and data['password'] == "admin":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})
@app.route('/')
def home():
    return "Backend is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)