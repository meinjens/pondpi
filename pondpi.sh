#!/bin/bash

cd /srv/pondpi
source /srv/pondpi/.env/bin/activate

python3 start.py 2> /srv/pondpi/pondpi.log &
