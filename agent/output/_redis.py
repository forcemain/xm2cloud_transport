#! -*- coding: utf-8 -*-


import redis
from agent.output.base import register_as_handler


@register_as_handler(name='redis')
class Redis(redis.StrictRedis):
    _ins = None

    def __init__(self, *args, **kwargs):
        super(Redis, self).__init__(*args, **kwargs)
        self.debug = kwargs.pop('debug', False)

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Redis, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def push_data(self, data):
        pass
