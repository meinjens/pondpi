#!/usr/bin/python3

import os

# flask-sock needs a threaded worker (one thread per websocket). A single process
# keeps the GPIO state in one place.
os.execvp("gunicorn", [
    "gunicorn",
    "-w", "1",
    "--threads", "50",
    "-b", ":5000",
    "--access-logfile", "-",
    "--error-logfile", "-",
    "--preload",
    "pondpi:create_app()",
])
