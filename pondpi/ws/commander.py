import flask
from flask import current_app as app

from pondpi.ws import ws

@ws.route('/status')
def echo_socket(socket):
    app.logger.info('[commander] Getting ship status...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/speed/set')
def set_speed(socket):
    app.logger.debug('[commander] Setting speed and answering...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/speed/stop')
def stop(socket):
    app.logger.debug('[commander] Making a full stop...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/destination/set')
def set_home(socket):
    app.logger.debug('[commander] Setting home position...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/home/set')
def set_home(socket):
    app.logger.debug('[commander] Setting home position...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/home/return')
def return_to_home(socket):
    app.logger.debug('[commander] Returning to home...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/exploration/start')
def start_exploration(socket):
    app.logger.debug('[commander] Returning to home...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")

@ws.route('/exploration/stop')
def stop_exploration(socket):
    app.logger.debug('[commander] Stopping exploration...')
    message = socket.receive()
    app.logger.debug(message)
    socket.send("Sending ship parameter...")
