#! -*- coding: utf-8 -*-


AGENT_INPUT = [
    {
        'engine': 'tcp',
        'conf': {
            'host': '0.0.0.0',
            'port': 8998
        }
    },
    {
        'engine': 'udp',
        'conf': {
            'host': '0.0.0.0',
            'port': 8999
        }
    },
    {
        'engine': 'jsonrpc',
        'conf': {
            'host': '10.2.5.51',
            'port': 9353,
            'username': 'limanman',
            'password': 'xmcloudsuperuser',
            'requests': [
                {'method': 'xmcloud/service/node/stat', 'params': ''},
                {'method': 'xmcloud/service/domain/stat', 'params': ''}
            ]
        }
    }
]

AGENT_FILTER = [
    {
        'engine': 'default',
        'conf': {
            'debug': True
        }
    },
]

AGENT_OUTPUT = [
    {
        'engine': 'default',
        'conf': {
            'debug': True
        }
    },
    {
        'engine': 'redis',
        'conf': {
            'host': '10.2.5.51',
            'port': 5123,
            'db': 0,
            'decode_responses': True
        }
    }
]
