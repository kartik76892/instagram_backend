from flask import Flask, request, jsonify
from flask_cors import CORS
import instaloader
import os
import requests

app = Flask(__name__)
CORS(app, origins=["https://instagram-frontend-topaz.vercel.app"])

@app.route('/api/followers', methods=['POST'])
def get_followers():
    data = request.get_json()
    username = data.get('username')


url = "https://instagram230.p.rapidapi.com/user/details"

querystring = {"username":username}

headers = {
	"x-rapidapi-key": "3357c42dcbmshd92e678d4f5e136p1eae7fjsnc9b368c274c8",
	"x-rapidapi-host": "instagram230.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
    return jsonify({'followers': response.edge_followed_by.count})

@app.route('/')
def home():
    return "Backend running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
