from flask import Flask, jsonify

app = Flask(__name__)

pictures = [
    {"id":1,"name":"concert1.jpg"},
    {"id":2,"name":"concert2.jpg"}
]

@app.route("/pictures")
def get_pictures():
    return jsonify(pictures)

@app.route("/health")
def health():
    return {"status":"ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
