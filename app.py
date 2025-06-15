from flask import Flask, render_template
import os

app = Flask(__name__)

SECRET_PATH = "/mnt/secrets/secret.txt"

@app.route("/")
def index():
    try:
        with open(SECRET_PATH, "r") as f:
            secret_value = f.read().strip()
            return render_template("success.html", secret=secret_value)
    except Exception:
        return render_template("error.html"), 500
