#!/usr/bin/env bash
echo "Starting Backend..."
pip install -r requirements.txt
gunicorn --workers=4 "src:create_app()" -b 0.0.0.0:8000