# Movie Directory App

A web app that does searches of movies.

Uses [The Movie Database API](https://developers.themoviedb.org/3/getting-started) (*requires an API key*).

## Prerequisities

This app is built using [Python 3](https://www.python.org/), [Flask](http://flask.pocoo.org/), and [Jinja](http://jinja.pocoo.org/) (as of 1/2019).

Requires an API key from [The Movie Database API](https://developers.themoviedb.org/3/getting-started). Sign up is free but they do ask for more contact information than seems necessary.

The server file is set to retrieve the API from an environment variable. To store the key in your environment:

```
export MOVIE_DB_APIKEY='<your API key here>'
```

You can also set the API key inside the ```server.py``` file by replacing ```os.environ['MOVIE_DB_APIKEY']``` with your API key.

### Installation

*Recommend using virtualenv when developing.*

```
$ pip3 install virtualenv
$ git clone https://github.com/memuunkie/movie_db_app.git
$ python3 -m venv movie_db_app/
$ cd movie_db_app/
$ virtualenv env
$ source env/bin/activate
$ deactivate [to leave virtualenv]
```

If you have virtualenv already installed, you can ignore the ```pip install```.

Install requirements to your environment.

```
$ pip3 install -r requirements.txt
```

### Debug Mode

This app uses [Flask Debug Toolbar](https://flask-debugtoolbar.readthedocs.io/en/latest/) to help during development and testing. 

When there is a ```redirect```, debug mode will put up a "Redirect (302)" with a link to the redirect page. This is good because it means things are working, but it can be jarring.

To turn off debug mode, set ```app.debug``` to ```False```.

### Running App Locally

In the terminal, run:
```
$ python server.py
```

The app defaults to [http://localhost:5000/](http://localhost:5000/). You can change the port by updating ```app.run()``` to your preferred port on ```server.py```.


## APIs Used

* [The Movie Database API](https://developers.themoviedb.org/3/getting-started)
