#!/usr/bin/python3

import os
import logging as log
import sys

log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "INFO"))

start_command="".join([
    "gunicorn -w 4 -b :5000 ",
    "--access-logfile - ",
    "--error-logfile - ",
    "--preload ",
    "-k flask_sockets.worker ",
    "'pondpi:create_app()'"])

os.system(start_command)
