#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt > /dev/null 2>&1
python3 crawler.py