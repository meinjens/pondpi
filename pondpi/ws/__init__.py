from flask import Flask, Blueprint

ws = Blueprint(r'ws', __name__)

from pondpi.ws import commander
