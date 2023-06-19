#!/usr/bin/env bash
# exit on error
set -o errexit

export GOOGLE_CLOUD_PROJECT=wisharoo
export USE_CLOUD_SQL_AUTH_PROXY=true

./cloud-sql-proxy wisharoo:us-central1:wisharoo --port 5433