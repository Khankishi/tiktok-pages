import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

CLIENT_KEY = os.environ.get("awuh6fdcvxl1a5c0")
CLIENT_SECRET = os.environ.get("xSqb3gf3pBSNMLj3Rw0FefwSFsQZTccY")
REDIRECT_URI = os.environ.get("TIKTOK_REDIRECT_URI")

@app.route("/")
def home():
    return "Backend OK ✅"

@app.route("/auth/tiktok/callback")
def tiktok_callback():
    code = request.args.get("code")
    if not code:
        return "No code", 400

    token_url = "https://open.tiktokapis.com/v2/oauth/token/"
    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }

    r = requests.post(token_url, data=data)
    return jsonify(r.json())
