#! -*- coding: utf-8 -*-

import logging
import threading


from SocketServer import StreamRequestHandler
from agent.input.base import register_as_handler
from agent.libs.socket_server.adapter import Server


class State(object):
    mark = None
    # for UdpServerRequestHandler use
    queue = None
    # for judge server is running
    isrun = False
    debug = False


class TcpServerRequestHandler(StreamRequestHandler):
    def handle(self):
        # for debug
        # client_addr = self.request.getpeername()
        # server_addr = self.request.getsockname()

        while True:
            line = self.rfile.readline()
            if not line.strip():
                break
            fmtdata = (self.__class__.__name__, self.handle.__name__, line)
            msgdata = 'input-{0}-handler-{1} recv data, data={2}'.format(*fmtdata)
            State.debug and logging.debug(msgdata)

            filter_data = {
                'mark': State.mark,
                'data': line
            }

            State.queue.put(filter_data)

        # close socket fd
        self.rfile.close()
        self.wfile.close()
        self.request.close()


@register_as_handler(name='tcp')
class TcpServer(object):
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
            self.serv = Server('nbttcp')
            self.serv.reg_request_handler(TcpServerRequestHandler)
            self.start()
        else:
            self.debug and logging.warning('{0} has already running, ignore'.format(self.__class__.__name__))

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(TcpServer, cls).__new__(cls, *args, **kwargs)

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
