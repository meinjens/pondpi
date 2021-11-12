import flask
from flask import current_app as app

from pondpi.ws import ws

@ws.route('/status')
def echo_socket(socket):
    while not socket.closed:
        message = socket.receive()
        app.logger.info('[commander] Getting ship status...')
        socket.send(message)

@ws.route('/steering/left')
def steering_left(socket):
    while not socket.closed:
        message = socket.receive()
        app.logger.info('[commander] Steering left')
        app.logger.info(message)
        socket.send(message)

@ws.route('/steering/right')
def steering_right(socket):
    while not socket.closed:
        message = socket.receive()
        app.logger.info('[commander] Steering right')
        app.logger.info(message)
        socket.send(message)

