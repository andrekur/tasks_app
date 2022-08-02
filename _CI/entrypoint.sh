#!/bin/sh
sleep 15

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:3000