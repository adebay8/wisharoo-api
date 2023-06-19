#!/usr/bin/env bash
# exit on error
set -o errexit

export GOOGLE_CLOUD_PROJECT=wisharoo
export USE_CLOUD_SQL_AUTH_PROXY=true

python3 manage.py runserver