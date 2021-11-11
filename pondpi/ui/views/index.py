import flask

from pondpi.ui import ui


@ui.route('/', methods=["GET"])
def index():
    return flask.render_template('start.html')

@ui.route('/dashboard', methods=["GET"])
def dashboard():
    return flask.render_template('dashboard.html')

@ui.route('/control-station', methods=["GET"])
def control_station():
    return flask.render_template('control-station.html')
