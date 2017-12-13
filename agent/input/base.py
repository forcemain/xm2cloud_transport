#! -*- coding: utf-8 -*-


import logging


class Input(object):
    _ins = None

    def __init__(self):
        self.queue = None
        self.handlers = {}

    def set_res_queue(self, queue):
        self.queue = queue

    def register_handler(self, name, handler):
        self.handlers[name] = handler

        fmtdata = (self.__class__.__name__, name, handler.__name__)
        logging.debug('{0} auto load plugin {1}, {2}'.format(*fmtdata))

    def create_engine(self, engine, conf):
        handler = self.handlers.get(engine)

        assert self.queue is not None

        conf['queue'] = self.queue

        return handler(**conf)


input_ins = Input()


def register_as_handler(name):
    def wrapper(cls):
        input_ins.register_handler(name, cls)
        # for handler class __new__ used
        return cls
    return wrapper
