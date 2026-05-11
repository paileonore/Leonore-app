from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "project": "Leonore Recon"
    })

@app.route('/api/username/<username>')
def username_lookup(username):

    results = [
        {
            "site": "Instagram",
            "status": "found"
        },
        {
            "site": "Twitter",
            "status": "not_found"
        },
        {
            "site": "GitHub",
            "status": "found"
        }
    ]

    return jsonify({
        "query": username,
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=True)
