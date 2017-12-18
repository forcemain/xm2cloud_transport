#! -*- coding: utf-8 -*-


import logging
import threading


from SocketServer import DatagramRequestHandler
from agent.input.base import register_as_handler
from agent.libs.socket_server.adapter import Server


class State(object):
    mark = None
    # for TcpServerRequestHandler use
    queue = None
    # for judge server is running
    isrun = False
    debug = False


class UdpServerRequestHandler(DatagramRequestHandler):
    def handle(self):
        # for debug
        # client_host, client_port = self.client_address

        line = self.rfile.readline()
        fmtdata = (self.__class__.__name__, self.handle.__name__, line)
        msgdata = 'input-{0}-handler-{1} recv data, data={2}'.format(*fmtdata)
        State.debug and logging.debug(msgdata)

        filter_data = {
            'mark': State.mark,
            'data': line
        }

        State.queue.put(filter_data)


@register_as_handler(name='udp')
class UdpServer(object):
    _ins = None

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', '0.0.0.0')
        self.port = kwargs.get('port', 8998)
        self.state = State

        # for write data back when recv data
        self.state.mark = kwargs.get('mark', 'default')
        self.state.queue = self.queue = kwargs.get('queue')
        self.state.debug = self.debug = kwargs.get('debug', False)

        if self.state.isrun is False:
            self.serv = Server('nbtudp')
            self.serv.reg_request_handler(UdpServerRequestHandler)
            self.start()
        else:
            self.debug and logging.warning('{0} has already running, ignore'.format(self.__class__.__name__))

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(UdpServer, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def start(self):
        def target():
            self.serv.run(self.host, self.port)

        t = threading.Thread(target=target)
        t.setDaemon(True)
        t.start()

        self.state.isrun = True

    def pull_data(self):
        pass
