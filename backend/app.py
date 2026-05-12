from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# USERNAME SEARCH
@app.route("/api/username/<username>")
def username(username):
    sites = [
        f"https://github.com/{username}",
        f"https://instagram.com/{username}",
        f"https://twitter.com/{username}",
        f"https://tiktok.com/@{username}"
    ]

    results = []

    for site in sites:
        try:
            r = requests.get(site, timeout=5)

            if r.status_code == 200:
                results.append({
                    "site": site,
                    "status": "found"
                })
            else:
                results.append({
                    "site": site,
                    "status": "not_found"
                })

        except:
            results.append({
                "site": site,
                "status": "error"
            })

    return jsonify(results)

# EMAIL SEARCH
@app.route("/api/email/<email>")
def email(email):
    return jsonify([
        {
            "site": "Google",
            "status": "found"
        },
        {
            "site": "Facebook",
            "status": "not_found"
        }
    ])

# PHONE SEARCH
@app.route("/api/phone/<phone>")
def phone(phone):
    return jsonify([
        {
            "site": "WhatsApp",
            "status": "found"
        },
        {
            "site": "Telegram",
            "status": "found"
        }
    ])

# DOMAIN SEARCH
@app.route("/api/domain/<domain>")
def domain(domain):
    return jsonify([
        {
            "site": "IP Lookup",
            "status": "found"
        },
        {
            "site": "DNS Records",
            "status": "found"
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)
