from flask import current_app as app

from pondpi.ws import sock


def _echo(socket, action):
    while True:
        message = socket.receive()
        app.logger.info('[commander] %s', action)
        app.logger.info(message)
        socket.send(message)


@sock.route('/ws/status')
def status(socket):
    _echo(socket, 'Getting ship status...')


@sock.route('/ws/steering/left')
def steering_left(socket):
    _echo(socket, 'Steering left')


@sock.route('/ws/steering/right')
def steering_right(socket):
    _echo(socket, 'Steering right')
