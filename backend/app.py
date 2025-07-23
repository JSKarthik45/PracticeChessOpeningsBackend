from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

STOCKFISH_PATH = r"./stockfish/stockfish-ubuntu-x86-64-avx2"

def get_best_move(fen, depth=15):
    p = subprocess.Popen(
        [STOCKFISH_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )
    cmds = f"uci\nisready\nposition fen {fen}\ngo depth {depth}\n"
    p.stdin.write(cmds)
    p.stdin.flush()
    bestmove = None
    while True:
        line = p.stdout.readline()
        if line.startswith("bestmove"):
            bestmove = line.split()[1]
            break
    p.stdin.close()
    p.stdout.close()
    p.terminate()
    return bestmove

@app.route("/", methods=["POST"])
def move():
    data = request.get_json()
    fen = data.get("fen")
    depth = data.get("depth", 15)
    if not fen:
        return jsonify({"error": "FEN required"}), 400
    move = get_best_move(fen, depth)
    return jsonify({"bestmove": move})


if __name__ == "__main__" :
    app.run()