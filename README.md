# xm2cloud_event_agent
#### 简单介绍:
>[xm2cloud_event_agent](https://github.com/xmdevops/xm2cloud_event_agent) 主要模拟Logstash软件架构实现的New_P2P监控Agent,兼容PY2.6+

***


#### 开发环境:
> SY_ENV: MacOS 10.12.6 \
> PY_ENV: Python2.7.10 

***

#### 快速安装:
`git clone https://github.com/xmdevops/xm2cloud_event_agent` \
`cd xm2cloud_event_agent` \
`python manage.py` 

***

#### 主要组件:
* input,已默认实现jsonrpc/tcp/udp处理器,支持装饰器自动注册自定义处理器
* filter,已默认实现default/xmcloud3_service_jsonrpc处理器,支持装饰器自动注册自定义处理器
* output,已默认实现default/redis/graphite处理器,支持装饰器自动注册自定义处理器

#### 更新日志:
* 2017-12-18 将Carbon/JsonRpc Client统一改为长连接模式,避免不必要的开销
* 2017-12-18 为filter组件新增xmcloud3_service_jsonrpc处理器,处理xmcloud平台服务监控数据
* 2017-12-18 为output组件新增graphite处理器,支持批量指标压缩发送
* 2017-12-18 支持所有组件DEBUG模式,方便调试,新增Metric规范以及范例

***

#### 配置文件:
```python
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
                'host': '123.59.27.192',
                'port': 2004,
                'debug': True
            }
        }
    ],

}
```

#### 运行日志:
```text
2017-12-18 18:35:31,130 - DEBUG - Agent start filter handlers ...
2017-12-18 18:35:31,131 - DEBUG - Agent start out handlers ...
2017-12-18 18:35:31,133 - DEBUG - Agent start input handlers ...
2017-12-18 18:35:31,133 - DEBUG - Agent start successfully!
2017-12-18 18:35:32,143 - DEBUG - JsonRpc.__auth_req_handler recv data, data={u'result': {u'username': u'limanman', u'nonce': u'62ozlr0pooi8ykgav12vcyg0u9osrxnu'}, u'id': 547288153, u'method': u'xmcloud/service/login'}
2017-12-18 18:35:34,312 - DEBUG - JsonRpc.__auth_req_handler recv data, data={u'result': {u'username': u'limanman', u'token': u'lrld1917i011nfrb5ro8d1o36bx0ua7o'}, u'id': 1112235364, u'method': u'xmcloud/service/login'}
2017-12-18 18:35:36,310 - DEBUG - JsonRpc.__domain_req_handler recv data, data={'data': {u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 6, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 15211}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 6, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 19578}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 20333}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 6, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 22423}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 23153}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 8, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 29642}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 8, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 32641}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 5, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 9612}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'band': 0, u'mem': 0, u'ip': u'123.59.27.192', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 3775}], u'id': 1678409640, u'method': u'xmcloud/service/domain/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:36,312 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/domain/stat', u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 15211, u'band': 6, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 19578, u'band': 6, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 20333, u'band': 7, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 22423, u'band': 6, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 23153, u'band': 7, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 29642, u'band': 8, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 32641, u'band': 8, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 9612, u'band': 5, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'123.59.27.192', u'port': 3775, u'band': 0, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}], u'id': 1678409640}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:36,315 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593336, 99.0)), ('10-2-5-51.mem-max', (1513593336, 99.0)), ('10-2-5-51.cpu-max', (1513593336, 99.0)), ('10-2-5-51.band', (1513593336, 6.625)), ('10-2-5-51.band', (1513593336, 0.0)), ('10-2-5-51.cpu', (1513593336, 0.0)), ('10-2-5-51.cpu', (1513593336, 0.0)), ('10-2-5-51.cpu-max', (1513593336, 99.0)), ('10-2-5-51.mem', (1513593336, 99.0)), ('10-2-5-51.mem', (1513593336, 99.0)), ('10-2-5-51.band-max', (1513593336, 300000.0)), ('10-2-5-51.band-max', (1513593336, 300000.0)), ('10-2-5-51.natsvr.conns', (1513593336, 0)), ('10-2-5-51.proxysvr.conns', (1513593336, 0)), ('10-2-5-51.natsvr.conns-max', (1513593336, 100000)), ('10-2-5-51.pssvr.conns', (1513593336, 0)), ('10-2-5-51.proxysvr.conns-max', (1513593336, 200)), ('10-2-5-51.nattestsvr.conns', (1513593336, 0)), ('10-2-5-51.nattestsvr.conns-max', (1513593336, 0)), ('10-2-5-51.logsvr.conns', (1513593336, 0)), ('10-2-5-51.datasvr.conns', (1513593336, 0)), ('10-2-5-51.webrtcsvr.conns', (1513593336, 0)), ('10-2-5-51.webrtcsvr.conns-max', (1513593336, 0)), ('10-2-5-51.logsvr.conns-max', (1513593336, 0)), ('10-2-5-51.pssvr.conns-max', (1513593336, 10000)), ('10-2-5-51.datasvr.conns-max', (1513593336, 0))], 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,310 - DEBUG - JsonRpc.__node_req_handler recv data, data={'data': {u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'master', u'port': 9255}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'', u'port': 32448}], u'id': 1562103759, u'method': u'xmcloud/service/node/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,310 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/node/stat', u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 9255, u'band': 0, u'cpu-max': 99, u'type': u'master', u'cpu': 0}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 32448, u'band': 0, u'cpu-max': 99, u'type': u'', u'cpu': 0}], u'id': 1562103759}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,311 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593340, 99.0)), ('10-2-5-51.cpu-max', (1513593340, 99.0)), ('10-2-5-51.band', (1513593340, 0.0)), ('10-2-5-51.cpu', (1513593340, 0.0)), ('10-2-5-51.mem', (1513593340, 99.0)), ('10-2-5-51.band-max', (1513593340, 300000.0))], 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,354 - DEBUG - JsonRpc.__node_req_handler recv data, data={'data': {u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'master', u'port': 9255}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'', u'port': 32448}], u'id': 654482847, u'method': u'xmcloud/service/node/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,354 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/node/stat', u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 9255, u'band': 0, u'cpu-max': 99, u'type': u'master', u'cpu': 0}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 32448, u'band': 0, u'cpu-max': 99, u'type': u'', u'cpu': 0}], u'id': 654482847}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,355 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593340, 99.0)), ('10-2-5-51.cpu-max', (1513593340, 99.0)), ('10-2-5-51.band', (1513593340, 0.0)), ('10-2-5-51.cpu', (1513593340, 0.0)), ('10-2-5-51.mem', (1513593340, 99.0)), ('10-2-5-51.band-max', (1513593340, 300000.0))], 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,398 - DEBUG - JsonRpc.__domain_req_handler recv data, data={'data': {u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 15211}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 19578}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'band': 6, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 20333}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 6, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 22423}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 8, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 23153}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 29642}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 32641}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 9612}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'band': 0, u'mem': 0, u'ip': u'123.59.27.192', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 3775}], u'id': 1296258101, u'method': u'xmcloud/service/domain/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,399 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/domain/stat', u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 15211, u'band': 7, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 19578, u'band': 7, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 20333, u'band': 6, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 22423, u'band': 6, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 23153, u'band': 8, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 29642, u'band': 7, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 32641, u'band': 7, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 9612, u'band': 7, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'123.59.27.192', u'port': 3775, u'band': 0, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}], u'id': 1296258101}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:40,400 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593340, 99.0)), ('10-2-5-51.mem-max', (1513593340, 99.0)), ('10-2-5-51.cpu-max', (1513593340, 99.0)), ('10-2-5-51.band', (1513593340, 6.875)), ('10-2-5-51.band', (1513593340, 0.0)), ('10-2-5-51.cpu', (1513593340, 0.0)), ('10-2-5-51.cpu', (1513593340, 0.0)), ('10-2-5-51.cpu-max', (1513593340, 99.0)), ('10-2-5-51.mem', (1513593340, 99.0)), ('10-2-5-51.mem', (1513593340, 99.0)), ('10-2-5-51.band-max', (1513593340, 300000.0)), ('10-2-5-51.band-max', (1513593340, 300000.0)), ('10-2-5-51.natsvr.conns', (1513593340, 0)), ('10-2-5-51.proxysvr.conns', (1513593340, 0)), ('10-2-5-51.natsvr.conns-max', (1513593340, 100000)), ('10-2-5-51.pssvr.conns', (1513593340, 0)), ('10-2-5-51.proxysvr.conns-max', (1513593340, 200)), ('10-2-5-51.nattestsvr.conns', (1513593340, 0)), ('10-2-5-51.nattestsvr.conns-max', (1513593340, 0)), ('10-2-5-51.logsvr.conns', (1513593340, 0)), ('10-2-5-51.datasvr.conns', (1513593340, 0)), ('10-2-5-51.webrtcsvr.conns', (1513593340, 0)), ('10-2-5-51.webrtcsvr.conns-max', (1513593340, 0)), ('10-2-5-51.logsvr.conns-max', (1513593340, 0)), ('10-2-5-51.pssvr.conns-max', (1513593340, 10000)), ('10-2-5-51.datasvr.conns-max', (1513593340, 0))], 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,352 - DEBUG - JsonRpc.__node_req_handler recv data, data={'data': {u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'master', u'port': 9255}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'band': 0, u'mem': 0, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'type': u'', u'port': 32448}], u'id': 477021240, u'method': u'xmcloud/service/node/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,354 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/node/stat', u'result': [{u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 9255, u'band': 0, u'cpu-max': 99, u'type': u'master', u'cpu': 0}, {u'node': u'dnssvr', u'band-max': 300000, u'domain': u'dnssvr.root', u'mem-max': 99, u'mem': 0, u'ip': u'120.92.118.162', u'port': 32448, u'band': 0, u'cpu-max': 99, u'type': u'', u'cpu': 0}], u'id': 477021240}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,354 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593345, 99.0)), ('10-2-5-51.cpu-max', (1513593345, 99.0)), ('10-2-5-51.band', (1513593345, 0.0)), ('10-2-5-51.cpu', (1513593345, 0.0)), ('10-2-5-51.mem', (1513593345, 99.0)), ('10-2-5-51.band-max', (1513593345, 300000.0))], 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,397 - DEBUG - JsonRpc.__domain_req_handler recv data, data={'data': {u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 8, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 15211}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 5, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 19578}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 20333}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 8, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 22423}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 5, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 23153}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 29642}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 32641}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 7, u'mem': 14, u'ip': u'120.92.118.162', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 9612}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'band': 0, u'mem': 0, u'ip': u'123.59.27.192', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 3775}], u'id': 1001954285, u'method': u'xmcloud/service/domain/stat'}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,397 - DEBUG - filter-Xmcloud3ServiceJsonRpc-handler-filter_data got data, data={'data': {u'method': u'xmcloud/service/domain/stat', u'result': [{u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 15211, u'band': 8, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 19578, u'band': 5, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 20333, u'band': 7, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 22423, u'band': 8, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 23153, u'band': 5, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 29642, u'band': 7, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 32641, u'band': 7, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'mem-max': 99, u'mem': 14, u'ip': u'120.92.118.162', u'port': 9612, u'band': 7, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'cpu': 0}, {u'node': u'webrtcsvr', u'band-max': 300000, u'domain': u'webrtcsvr.cn', u'mem-max': 99, u'mem': 0, u'ip': u'123.59.27.192', u'port': 3775, u'band': 0, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'cpu': 0}], u'id': 1001954285}, 'mark': 'xmcloud3_service_jsonrpc'}
2017-12-18 18:35:45,398 - DEBUG - output-Graphite-handler-push_data got data, data={'data': [('10-2-5-51.mem-max', (1513593345, 99.0)), ('10-2-5-51.mem-max', (1513593345, 99.0)), ('10-2-5-51.cpu-max', (1513593345, 99.0)), ('10-2-5-51.band', (1513593345, 6.75)), ('10-2-5-51.band', (1513593345, 0.0)), ('10-2-5-51.cpu', (1513593345, 0.0)), ('10-2-5-51.cpu', (1513593345, 0.0)), ('10-2-5-51.cpu-max', (1513593345, 99.0)), ('10-2-5-51.mem', (1513593345, 99.0)), ('10-2-5-51.mem', (1513593345, 99.0)), ('10-2-5-51.band-max', (1513593345, 300000.0)), ('10-2-5-51.band-max', (1513593345, 300000.0)), ('10-2-5-51.natsvr.conns', (1513593345, 0)), ('10-2-5-51.proxysvr.conns', (1513593345, 0)), ('10-2-5-51.natsvr.conns-max', (1513593345, 100000)), ('10-2-5-51.pssvr.conns', (1513593345, 0)), ('10-2-5-51.proxysvr.conns-max', (1513593345, 200)), ('10-2-5-51.nattestsvr.conns', (1513593345, 0)), ('10-2-5-51.nattestsvr.conns-max', (1513593345, 0)), ('10-2-5-51.logsvr.conns', (1513593345, 0)), ('10-2-5-51.datasvr.conns', (1513593345, 0)), ('10-2-5-51.webrtcsvr.conns', (1513593345, 0)), ('10-2-5-51.webrtcsvr.conns-max', (1513593345, 0)), ('10-2-5-51.logsvr.conns-max', (1513593345, 0)), ('10-2-5-51.pssvr.conns-max', (1513593345, 10000)), ('10-2-5-51.datasvr.conns-max', (1513593345, 0))], 'mark': 'xmcloud3_service_jsonrpc'}

KeyboardInterrupt
...
```
***

#### 指标图示:
![metric&char.png](https://raw.githubusercontent.com/xmdevops/xm2cloud_event_agent/master/docs/design/metric%26char.png)
***

#### Copyright:
2017.12.13  (c) Limanman <xmdevops@vip.qq.com>

