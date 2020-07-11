#! /bin/bash

nginx -g 'daemon off;' &
python api.py &
