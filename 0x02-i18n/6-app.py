#!/usr/bin/env python3
"""the babel instance module"""
from typing import Dict, Union, Optional

from flask_babel import Babel, lazy_gettext as _l
from flask import Flask, render_template, request, g

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "fr", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Use request.accept_languages to determine the best
    match with our supported languages"""
    locale = request.args.get("locale", None)
    if locale is not None and locale in app.config["LANGUAGES"]:
        return locale
    locale = g.user.get("locale", None)
    if locale is not None and locale in app.config["LANGUAGES"]:
        return locale
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    hello.
    """
    return render_template('6-index.html')


def get_user() -> Optional[Dict]:
    """returns a mock user"""
    id = request.args.get("login_as", None)
    if id is None or int(id) not in users:
        return None
    return users[int(id)]


@app.before_request
def before_request():
    """gets a user and sets it to global"""
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
