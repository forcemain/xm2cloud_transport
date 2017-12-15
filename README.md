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
* filter,已默认实现default处理器,支持装饰器自动注册自定义处理器
* output,已默认实现default/redis处理器,支持装饰器自动注册自定义处理器

***

#### 主要配置:
```python
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
```

***

#### 运行日志:
```text
/usr/bin/python /Users/manmanli/xm-webs/public/xm2cloud_event_agent/manage.py
2017-12-13 20:39:09,040 - DEBUG - Agent start filter handlers ...
2017-12-13 20:39:09,041 - DEBUG - Agent start out handlers ...
2017-12-13 20:39:09,042 - DEBUG - Agent start input handlers ...
2017-12-13 20:39:09,042 - DEBUG - Agent start successfully!
2017-12-13 20:39:10,075 - DEBUG - JsonRpc.__auth_req_handler recv data, data={u'result': {u'username': u'limanman', u'nonce': u'w3380ad77wo01yoygfsy44g5yb90axzf'}, u'id': 896778532, u'method': u'xmcloud/service/login'}
2017-12-13 20:39:12,083 - DEBUG - JsonRpc.__auth_req_handler recv data, data={u'result': {u'username': u'limanman', u'token': u'tgp8ghlr1oitswk1dn275qg0gbt8k1ev'}, u'id': 1444644022, u'method': u'xmcloud/service/login'}
2017-12-13 20:39:14,086 - DEBUG - JsonRpc.__domain_req_handler recv data, data={u'result': [{u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 1356}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 27, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 30652}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 42782}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 46549}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 51341}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 9, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 57456}, {u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 25, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 63558}], u'id': 1339913011, u'method': u'xmcloud/service/domain/stat'}
2017-12-13 20:39:14,088 - DEBUG - filter-Default-handler-filter_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 27, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 9, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 25, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1339913011, "method": "xmcloud/service/domain/stat"}
2017-12-13 20:39:14,090 - DEBUG - output-Default-handler-push_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 27, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 9, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 25, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1339913011, "method": "xmcloud/service/domain/stat"}
2017-12-13 20:39:18,078 - WARNING - TcpServer has already running, ignore
2017-12-13 20:39:18,079 - WARNING - UdpServer has already running, ignore
2017-12-13 20:39:18,089 - DEBUG - JsonRpc.__node_req_handler recv data, data={u'result': [{u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 1356}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 27, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 30652}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 42782}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 46549}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 24, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 51341}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 9, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 57456}, {u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 25, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 1, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 63558}], u'id': 1435979342, u'method': u'xmcloud/service/node/stat'}
2017-12-13 20:39:18,090 - DEBUG - filter-Default-handler-filter_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 27, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 9, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 25, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1435979342, "method": "xmcloud/service/node/stat"}
2017-12-13 20:39:18,091 - DEBUG - output-Default-handler-push_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 27, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 24, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 9, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 25, "mem": 55, "ip": "10.2.5.51", "cpu": 1, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1435979342, "method": "xmcloud/service/node/stat"}
2017-12-13 20:39:18,092 - DEBUG - JsonRpc.__node_req_handler recv data, data={u'result': [{u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 1356}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 13, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 30652}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 42782}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 46549}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 51341}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 14, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 57456}, {u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 11, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 63558}], u'id': 233264442, u'method': u'xmcloud/service/node/stat'}
2017-12-13 20:39:18,092 - DEBUG - filter-Default-handler-filter_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 13, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 14, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 11, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 233264442, "method": "xmcloud/service/node/stat"}
2017-12-13 20:39:18,093 - DEBUG - output-Default-handler-push_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 13, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 14, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 11, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 233264442, "method": "xmcloud/service/node/stat"}
2017-12-13 20:39:18,095 - DEBUG - JsonRpc.__domain_req_handler recv data, data={u'result': [{u'node': u'pssvr', u'band-max': 300000, u'domain': u'pssvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 10000, u'conns': 0, u'type': u'master', u'port': 1356}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 13, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 30652}, {u'node': u'natsvr', u'band-max': 300000, u'domain': u'natsvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100000, u'conns': 0, u'type': u'master', u'port': 42782}, {u'node': u'datasvr', u'band-max': 300000, u'domain': u'datasvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 46549}, {u'node': u'nattestsvr', u'band-max': 300000, u'domain': u'nattestsvr.cn', u'band': 17, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 51341}, {u'node': u'proxysvr', u'band-max': 300000, u'domain': u'proxysvr.natsvr.cn', u'band': 14, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 100, u'conns': 0, u'type': u'master', u'port': 57456}, {u'node': u'logsvr', u'band-max': 300000, u'domain': u'logsvr.cn', u'band': 11, u'mem': 55, u'ip': u'10.2.5.51', u'cpu': 0, u'mem-max': 99, u'cpu-max': 99, u'conns-max': 0, u'conns': 0, u'type': u'master', u'port': 63558}], u'id': 1289907308, u'method': u'xmcloud/service/domain/stat'}
2017-12-13 20:39:18,095 - DEBUG - filter-Default-handler-filter_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 13, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 14, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 11, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1289907308, "method": "xmcloud/service/domain/stat"}
2017-12-13 20:39:18,097 - DEBUG - output-Default-handler-push_data got data, data={"result": [{"node": "pssvr", "band-max": 300000, "domain": "pssvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 10000, "conns": 0, "type": "master", "port": 1356}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 13, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 30652}, {"node": "natsvr", "band-max": 300000, "domain": "natsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100000, "conns": 0, "type": "master", "port": 42782}, {"node": "datasvr", "band-max": 300000, "domain": "datasvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 46549}, {"node": "nattestsvr", "band-max": 300000, "domain": "nattestsvr.cn", "band": 17, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 51341}, {"node": "proxysvr", "band-max": 300000, "domain": "proxysvr.natsvr.cn", "band": 14, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 100, "conns": 0, "type": "master", "port": 57456}, {"node": "logsvr", "band-max": 300000, "domain": "logsvr.cn", "band": 11, "mem": 55, "ip": "10.2.5.51", "cpu": 0, "mem-max": 99, "cpu-max": 99, "conns-max": 0, "conns": 0, "type": "master", "port": 63558}], "id": 1289907308, "method": "xmcloud/service/domain/stat"}

KeyboardInterrupt
...
```
***

#### Copyright:
2017.12.13  (c) Limanman <xmdevops@vip.qq.com>

