#!/usr/bin/bash

# get newest commits from github
git pull origin master

# activate the virtual environment
source venv/bin/activate

# install (new) requirements
pip install -r requirements.txt

# start flask server
python app/http-health-check/src/http_heartbeat_flask.py
