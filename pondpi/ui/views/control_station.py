import flask

from pondpi.ui import ui


@ui.route('/control-station', methods=["GET"])
def control_station():
    return flask.render_template('control-station.html')

