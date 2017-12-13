# -*- coding: utf-8 -


"""
1. for no_blocking socket entry
"""


from agent.libs.simple_http_parser.socketio import SocketIO


class SocketReader(SocketIO):
    def __init__(self, sock):
        super(SocketReader, self).__init__(sock, mode='rb')
