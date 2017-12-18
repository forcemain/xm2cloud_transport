#! -*- coding: utf-8 -*-


"""
AGENT_INPUT support handlers:
    [
        {
            'engine': 'tcp',
            'conf': {'mark': '', ...}
        },
        {
            'engine': 'udp',
            'conf': {'mark': '', ...}
        },
        {
            'engine': 'jsonrpc',
            'conf': {'mark': '', ...}
        },

        any more you custom, like jsonrpc
    ]


AGENT_FILTER support handlers:
    'default': [
        {
            'engine': 'default',
            'conf': { ... }
        },
    ],
    'xmcloud3_service_jsonrpc': [
        {
            'engine': '',
            'conf': { ... }
        }
    ]

    any more you custom, like xmcloud3_service_jsonrpc


AGENT_OUTPUT support handlers:
    [
        {
            'engine': 'default',
            'conf': { ... }
        },
        {
            'engine': 'redis',
            'conf': { ... }
        },
        {
            'engine': 'graphite',
            'conf': { ... }
        }
    ]

    any more you custom, like graphite
"""


AGENT_INPUT = [
    {
        'engine': 'jsonrpc',
        'conf': {
            'mark': 'xmcloud3_service_jsonrpc',
            'host': 'xmcloud.xmsecu.com',
            'port': 9353,
            'username': 'limanman',
            'password': 'xmcloudsuperuser',
            'requests': [
                {'method': 'xmcloud/service/node/stat', 'params': ''},
                {'method': 'xmcloud/service/domain/stat', 'params': ''}
            ],
            'debug': True
        }
    }
]

AGENT_FILTER = {
    'default': [
        {
            'engine': 'default',
            'conf': {
                'debug': True
            }
        },
    ],
    'xmcloud3_service_jsonrpc': [
        {
            'engine': 'xmcloud3_service_jsonrpc',
            'conf': {
                'debug': True
            }
        }
    ]
}

AGENT_OUTPUT = {
    'default': [
        {
            'engine': 'default',
            'conf': {
                'debug': True
            }
        }
    ],
    'xmcloud3_service_jsonrpc': [
        {
            'engine': 'graphite',
            'conf': {
                'host': '10.2.5.51',
                'port': 2004,
                'debug': True
            }
        }
    ],

}
