#!/usr/bin/sh
# use the same APPNAME in start-pytavia-web.sh
APPNAME=AUTH_SERVICES

pkill -f "gunicorn -n $APPNAME" && printf "Application $APPNAME has been stopped ...\n"
