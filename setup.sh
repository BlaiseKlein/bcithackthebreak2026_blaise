#!/bin/bash

python -m venv ./.venv
source ./.venv/bin/activate
pip install -r requirements.txt
cd ./GUI
python ./app.py
