# Pepita--Backend
This repo contains the implementation of the backend for the minimum viable product (MVP) of Pepita.

The backend is based on the [Flask framework](https://flask.palletsprojects.com/en/2.1.x/).

Initial setup:
1. Ensure `pip` is installed in your system
2. Create & activate a virtual environment using `pip`
3. Run `pip install -r requirements.txt` in the activated virtual environment

Commands:
### `python wsgi.py`
Runs the application in development mode. This requires:
 - A database server to be running at the time of starting the backend
 - A `.env` file with variables `DBUSER_DEV`, `DBPASS_DEV`, `DBHOST_DEV`, `DBNAME_DEV` defined.