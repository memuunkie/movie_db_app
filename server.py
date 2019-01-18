from jinja2 import StrictUndefined

from flask import jsonify
from flask import (Flask, render_template, redirect, request, flash, session, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime

import os

import requests

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY']= "ABCItseasyas123orsimpleasDo-Re-MiABC123babyyouandmegirl"

app.jinja_env.undefined = StrictUndefined

# TODO: put into environment variable
MOVIE_DB_APYKEY = "?api_key=d2081d54357f3eb6f9788eb96e93e156"

# for response data
payload = "{}"

# movie database base url
tmdb_url = "https://api.themoviedb.org/3/"

# for images: url + size + image filepath
img_base_url = "https://image.tmdb.org/t/p/"

# sizes for images
sm_img = "w92"
# maybe use "w154", "w342", "w500", w780", "original"
lg_img = "w185"

@app.route('/')
def index():
    """ Home page
        Lists out popular movies with image
    """
    image_url = img_base_url + sm_img
    request_url = tmdb_url + "movie/popular" + MOVIE_DB_APYKEY
    
    movies = requests.request("GET", request_url, data=payload).json()

    return render_template("home.html", movies=movies["results"], image_url=image_url)

@app.route('/details')
def get_details():
    """ Details page
        Details and info of individual movie
    """
    return


#################################################################
if __name__ == "__main__":
    # Have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode
    # add formatDatetime to Jinja template
    #app.jinja_env.filters['formatDatetime'] = formatDatetime

    # Use the DebugToolbar
    DebugToolbarExtension(app)


app.run(port=5000, host='0.0.0.0')