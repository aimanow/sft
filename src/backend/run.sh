#!/usr/bin/env bash

chown -r 0777 ./uploaded_files
#exec gunicorn3 "app:create_app()" --reload -b 0.0.0.0:5000
flask run --host=0.0.0.0