#! -*- coding: utf-8 -*-


import logging


from agent.filter.base import register_as_handler


@register_as_handler(name='default')
class Default(object):
    _ins = None

    def __init__(self, *args, **kwargs):
        self.debug = kwargs.get('debug', False)

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Default, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def filter_data(self, data):
        if self.debug is False:
            return data
        fmtdata = (self.__class__.__name__, self.filter_data.__name__, data)
        msgdata = 'filter-{0}-handler-{1} got data, data={2}'.format(*fmtdata)
        logging.debug(msgdata)

        return data
