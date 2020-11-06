"""Server for song snippet app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect, jsonify)
from jinja2 import StrictUndefined
import requests
import os

from model import connect_to_db
import crud

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/albums')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")