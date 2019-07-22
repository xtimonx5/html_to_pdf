#!/usr/bin/env bash

if [ $DEBUG = "true" ]; then
    gosu root /usr/sbin/sshd -D
else
    python manage.py runserver 0.0.0.0:8000
fi
