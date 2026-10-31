import logging as log
import sys
import os
from flask import Flask

from pondpi import ui, ws, ship

log.basicConfig(stream=sys.stderr, level=os.environ.get("LOG_LEVEL", "INFO"))


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.register_blueprint(ui.ui, url_prefix=r'/ui')
    ws.sock.init_app(app)

    return app
