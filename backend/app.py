from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def move():
    return jsonify({"bestmove": "a1"})

if __name__ == "__main__" :
    app.run()