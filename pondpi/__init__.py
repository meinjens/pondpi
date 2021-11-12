import logging as log
import sys
import os
from flask import Flask
from flask_sockets import Sockets

from pondpi import ui, ws, ship


log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "INFO"))

def create_app():
    app = Flask(__name__, static_folder='../static')
    sockets = Sockets(app)

    app.register_blueprint(ui.ui, url_prefix=r'/ui')
    sockets.register_blueprint(ws.ws, url_prefix=r'/ws')

    return app
