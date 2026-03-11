from flask import Flask, jsonify

app = Flask(__name__)

songs = [
    {"name":"Song A","lyrics":"La la la"},
    {"name":"Song B","lyrics":"Na na na"}
]

@app.route("/songs")
def get_songs():
    return jsonify(songs)

@app.route("/health")
def health():
    return {"status":"ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
