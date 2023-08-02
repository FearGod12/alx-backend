#!/usr/bin/env python3
"""the babel instance module
with config class and some other functions
"""
from datetime import datetime
from typing import Dict, Optional

import pytz
from flask_babel import Babel
from flask import Flask, render_template, request, g

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
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
    if g.user:
        locale = g.user.get("locale")
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
    return render_template('index.html')


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
    g.time = datetime.now(pytz.timezone(get_timezone())).\
        strftime('%b %d, %Y, %I:%M:%S %p')


@babel.timezoneselector
def get_timezone():
    """gets the user timezone"""
    timez = request.args.get("timezone")
    if timez is not None:
        try:
            zone = pytz.timezone(timez)
            return zone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user is not None:
        timez = g.user.get("timezone")
        try:
            zone = pytz.timezone(timez)
            return zone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
