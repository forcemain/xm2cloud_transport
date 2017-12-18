#! -*- coding: utf-8 -*-


import socket
import logging


from agent.libs.graphite.client import Client
from agent.output.base import register_as_handler


@register_as_handler(name='graphite')
class Graphite(Client):
    _ins = None

    def __init__(self, *args, **kwargs):
        super(Graphite, self).__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Graphite, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def push_data(self, data):
        if self.debug:
            fmtdata = (self.__class__.__name__, self.push_data.__name__, data)
            msgdata = 'output-{0}-handler-{1} got data, data={2}'.format(*fmtdata)
            logging.debug(msgdata)

        filter_mark, filter_data = data['mark'], data['data']
        self.write(filter_data)
