from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='../frontend/dist')

@app.route("/api/a")
def a() :
    return "a"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue_app(path):
    static_file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(static_file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__" :
    app.run()