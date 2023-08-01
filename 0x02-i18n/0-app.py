#!/usr/bin/env python3
"""Flask app module"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def get_hello() -> str:
    """
    hello    :return:  world
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
