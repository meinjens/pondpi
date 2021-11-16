#!/bin/bash

cd /srv/pondpi
source .venv/bin/activate

python3 start.py 2> /srv/pondpi/pondpi.log &
