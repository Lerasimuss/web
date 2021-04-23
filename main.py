from flask import Flask, render_template, redirect, request, make_response, session
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(port=random.randrange(1000, 9999), host='127.0.0.1')
