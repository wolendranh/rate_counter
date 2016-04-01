#!/usr/bin/env bash
cd rate_counter/
./manage.py celery worker -B --concurrency=1
