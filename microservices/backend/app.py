from flask import Flask

app = Flask(__name__)

@app.route("/api")
def api():
    return {"message": "Backend Running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)