#Movie Directory App

A web app that does searches of movies.

Uses [The Movie Database API](https://developers.themoviedb.org/3/getting-started) (*requires an API key*).

### Prerequisities

This app is built using Python 3 (as of 1/2019).

Requires an API key from [The Movie Database API](https://developers.themoviedb.org/3/getting-started). Sign up is free but they do ask for more contact information than seems necessary.

Recommend setting API key to environmental variable. 

```
export MOVIE_DB_APIKEY='[your API key here]'
```

*Recommend using virtualenv when developing.*

```
$ python3 -m venv movie_dir_app/
$ source env/bin/activate
```

Install requirements to your environment.

```
$ pip install -r requirements.txt
```
