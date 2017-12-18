#! -*- coding: utf-8 -*-


import time

from agent.input.base import register_as_handler
from agent.libs.p2p_jsonrpc.client import Client


@register_as_handler(name='jsonrpc')
class JsonRpc(Client):
    _ins = None

    def __init__(self, *args, **kwargs):
        super(JsonRpc, self).__init__(*args, **kwargs)
        self.requests = kwargs.get('requests', [])

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(JsonRpc, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def pull_data(self):
        if not self.requests:
            return

        while True:
            if self.state.nonce is not None:
                break
            self.auth_nonce()
            time.sleep(2)

        while True:
            if self.state.token is not None:
                break
            self.auth_login()
            time.sleep(2)

        for item in self.requests:
            self.query(**item)


