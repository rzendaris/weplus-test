# Rafi Zendaris

This is the backend for the Ajaib system.

This system uses:

* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) for the API endpoints.

* [pipenv](https://pipenv.readthedocs.io/en/latest/) for managing requirements.

* [Gunicorn](https://docs.gunicorn.org/en/stable/) for Python Web Server Gateway Interface.

* [SQLite3](https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/) for Database Engine.

## Dependency Setup

Setup your virtualenv:

1. Create a env using `Python==3.7`
    ```bash
    pipenv --python 3.7
    ```

2. Install the requirements from the `Pipfile`
    ```bash
    pipenv install
    ```

3. Run commands within pipenv shell
    ```bash
    pipenv shell
    ```

## Running Server

```bash
gunicorn wsgi:app
```
