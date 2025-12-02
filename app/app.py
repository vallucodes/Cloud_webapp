from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random():
    value = random.randint(1, 100)
    return jsonify({"number": value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
