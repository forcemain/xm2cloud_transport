#! -*- coding: utf-8 -*-

import socket
import struct
import pickle


from threading import Lock


class State(object):
    lock = Lock()
    connected = False

    @classmethod
    def re_connect(cls, host, port):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        cls.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        cls.sock.connect((host, port))


class Client(object):
    def __init__(self, *args, **kwargs):
        self.state = State
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.debug = kwargs.get('debug', False)

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Client, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def write(self, metrics=[]):
        with self.state.lock:
            if not self.state.connected:
                self.state.re_connect(self.host, self.port)
                self.state.connected = True

        payload = pickle.dumps(metrics, protocol=2)
        # for 4 bytes header，encapsulation package
        header = struct.pack('!L', len(payload))
        message = header + payload
        try:
            self.state.sock.sendall(message)
        except socket.error as e:
            self.state.connected = False
