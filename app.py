from flask import Flask, request, jsonify
from flask_cors import CORS
import instaloader
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/followers', methods=['POST'])
def get_followers():
    data = request.get_json()
    print("This is test", data)
    username = data.get('username')

    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return jsonify({'followers': profile.followers})
    except Exception:
        return jsonify({'followers': 0})

@app.route('/')
def home():
    return "Backend running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
