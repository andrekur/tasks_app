#!/bin/sh
sleep 15

CMD gunicorn app.wsgi:application --bind 0.0.0.0:3000