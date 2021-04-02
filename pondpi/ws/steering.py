import flask
from flask_sockets import Sockets

from pondpi.ws import ws

@ws.route('/echo')
def echo_socket(socket):
    while not socket.closed:
        message = socket.receive()
        print(message)
        socket.send(message)