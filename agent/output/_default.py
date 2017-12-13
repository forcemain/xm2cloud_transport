#! -*- coding: utf-8 -*-


import logging


from agent.output.base import register_as_handler


@register_as_handler(name='default')
class Default(object):
    _ins = None

    def __init__(self, debug=True):
        self.debug = debug

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Default, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def push_data(self, data):
        if self.debug is False:
            return
        fmtdata = (self.__class__.__name__, self.push_data.__name__, data)
        msgdata = 'output-{0}-handler-{1} got data, data={2}'.format(*fmtdata)
        logging.debug(msgdata)
