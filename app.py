from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/followers', methods=['POST'])
def get_followers():
    data = request.get_json()
    username = data.get('username')

    url = "https://instagram230.p.rapidapi.com/user/details"
    querystring = {"username": username}

    # headers = {
    #     "x-rapidapi-key": "3357c42dcbmshd92e678d4f5e136p1eae7fjsnc9b368c274c8",
    #     "x-rapidapi-host": "instagram230.p.rapidapi.com"
    # }
    headers = {
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY"),
    "x-rapidapi-host": "instagram230.p.rapidapi.com"
}


    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        #followers = data.get('edge_followed_by', {}).get('count', 0)
        return jsonify({'followers': data.edge_followed_by.count})
    except Exception as e:
        print("Error:", e)
        return jsonify({'followers': 0})

@app.route('/')
def home():
    return "Backend running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
