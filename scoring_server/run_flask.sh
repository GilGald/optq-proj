#!/usr/bin/env bash
export FLASK_APP=api/score_service_api.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080

