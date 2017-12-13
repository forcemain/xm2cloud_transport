#! -*- coding: utf-8 -*-


import logging


class Output(object):
    _ins = None

    def __init__(self):
        self.handlers = {}

    def register_handler(self, name, handler):
        self.handlers[name] = handler

        fmtdata = (self.__class__.__name__, name, handler.__name__)
        logging.debug('{0} auto load plugin {1}, {2}'.format(*fmtdata))

    def create_engine(self, engine, conf):
        handler = self.handlers.get(engine)

        return handler(**conf)


output_ins = Output()


def register_as_handler(name):
    def wrapper(cls):
        output_ins.register_handler(name, cls)
        # for handler class __new__ used
        return cls
    return wrapper
