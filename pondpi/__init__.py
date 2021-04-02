import logging as log
import sys
import os
import flask
from flask_sockets import Sockets

from pondpi import ui, ws


log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "INFO"))

def create_app():
    app = flask.Flask(__name__, static_folder='../static')
    sockets = Sockets(app)

    app.register_blueprint(ui.ui, url_prefix='/ui')
    sockets.register_blueprint(ws.ws, url_prefix='/ws')

    return app
