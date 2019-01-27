# server.py - Server file for movie discovery app
#
# Description:
# ------------
# Provides server-side functionality for index, get_details, and search routes.
# Returns list of popular movies ('/'), details on individual movies ('/details/<movie_id>'),
# and searchs for movies in TMDB ('search')
#
# Todo: 
# -----
# - Tests
#
# Changelog:
# ----------
# 01a, 2019-01-19, MAL - First functional commit

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime

import os

import requests

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY']= "ABCItseasyas123orsimpleasDo-Re-MiABC123babyyouandmegirl"

app.jinja_env.undefined = StrictUndefined

# get API key from environment
MOVIE_DB_APIKEY = "?api_key=" + os.environ['MOVIE_DB_APIKEY']

# for response data, per TMDB docs
payload = "{}"

# movie database base url
tmdb_url = "https://api.themoviedb.org/3/"

# for images: url + size + image filepath
img_base_url = "https://image.tmdb.org/t/p/"

# sizes for images
sm_img = "w154"
lg_img = "w185"

@app.route('/')
def index():
    """ Home page
        Lists out popular movies with image
    """
    image_url = img_base_url + sm_img
    request_url = tmdb_url + "movie/popular" + MOVIE_DB_APIKEY
    
    movies = requests.request("GET", request_url, data=payload).json()

    return render_template("home.html", movies=movies["results"], image_url=image_url)

@app.route('/details/<movie_id>', methods=['GET'])
def get_details(movie_id):
    """ Details page
        Details and info of individual movie
    """
    image_url = img_base_url + lg_img
    request_url = tmdb_url + "movie/" + movie_id + MOVIE_DB_APIKEY

    movie = requests.request("GET", request_url, data=payload).json()

    return render_template("details.html", movie=movie, image_url=image_url)

@app.route('/search', methods=['GET'])
def search():
    """ Search
        Querys against TMDB data
    """
    if request.args.get('searchTerms') == "":
        return redirect("/")

    query = "&query=" + request.args.get('searchTerms')

    image_url = img_base_url + sm_img
    request_url = tmdb_url + "search/movie" + MOVIE_DB_APIKEY + query

    movies = requests.request("GET", request_url, data=payload).json()

    return render_template("search.html", movies=movies["results"], image_url=image_url)

#################################################################
if __name__ == "__main__":
    # Have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    DebugToolbarExtension(app)


app.run(port=5000, host='0.0.0.0')  