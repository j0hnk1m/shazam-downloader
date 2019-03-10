#!/bin/bash

pip3 install pipenv
pipenv install --ignore-pipfile
pipenv shell
python3 main.py
