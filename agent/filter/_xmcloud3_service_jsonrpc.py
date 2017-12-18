#! -*- coding: utf-8 -*-


from __future__ import division


import json
import time
import logging


from agent.filter.base import register_as_handler


class Basics(object):
    def __init__(self, ip=None, cpu=None, cpu_max=None, mem=None, mem_max=None, band=None, band_max=None):
        self.ip = ip
        self.cpu = cpu
        self.cpu_max = cpu_max
        self.mem = mem
        self.mem_max = mem_max
        self.band = band
        self.band_max = band_max

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_cpu(self):
        return self.cpu

    def set_cpu(self, cpu):
        self.cpu = cpu

    def get_cpu_max(self):
        return self.cpu_max

    def set_cpu_max(self, cpu_max):
        self.cpu_max = cpu_max

    def get_mem(self):
        return self.mem

    def set_mem(self, mem):
        self.mem = mem

    def get_mem_max(self):
        return self.mem_max

    def set_mem_max(self, mem_max):
        self.mem_max = mem_max

    def get_band(self):
        return  self.band

    def set_band(self, band):
        self.band = band

    def get_band_max(self):
        return self.band_max

    def set_band_max(self, band_max):
        self.band_max = band_max

    def to_dict(self):
        dict_data = {
            'ip': self.get_ip(),
            'cpu': self.get_cpu(),
            'cpu-max': self.get_cpu_max(),
            'mem': self.get_cpu_max(),
            'mem-max': self.get_mem_max(),
            'band': self.get_band(),
            'band-max': self.get_band_max()
        }

        return dict_data

    def to_json(self):
        json_data = json.dumps(self.to_dict())

        return json_data

    def to_metrics(self):
        metrics = []
        dict_data = self.to_dict()
        for key in dict_data:
            val = dict_data[key]
            if val is None:
                continue
            if key == 'ip':
                continue
            mtimestamp = int(time.time())
            metric_key = '{0}.{1}'.format(self.ip.replace('.', '-'), key)

            metrics.append((metric_key, (mtimestamp, val)))

        return metrics

    @staticmethod
    def from_dict(dict_data):
        ip = dict_data.get('ip', None)
        cpu = dict_data.get('cpu', None)
        cpu_max = dict_data.get('cpu-max', None)
        mem = dict_data.get('mem', None)
        mem_max = dict_data.get('mem-max', None)
        band = dict_data.get('band', None)
        band_max = dict_data.get('band-max', None)

        return Basics(ip=ip, cpu=cpu, cpu_max=cpu_max, mem=mem, mem_max=mem_max, band=band, band_max=band_max)

    @staticmethod
    def from_json(json_data):
        dict_data = json.loads(json_data)

        return Basics.from_dict(dict_data)


class Business(object):
    def __init__(self, ip=None, node=None, conns=None, conns_max=None):
        self.ip = ip
        self.node = node
        self.conns = conns
        self.conns_max = conns_max

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def get_conns(self):
        return self.conns

    def set_conns(self, conns):
        self.conns = conns

    def get_conns_max(self):
        return self.conns_max

    def set_conns_max(self, conns_max):
        self.conns_max = conns_max

    def to_dict(self):
        dict_data = {
            'ip': self.get_ip(),
            'node': self.get_node(),
            'conns': self.get_conns(),
            'conns-max': self.get_conns_max()
        }

        return dict_data

    def to_json(self):
        dict_data = self.to_dict()
        json_data = json.dumps(dict_data)

        return json_data

    def to_metrics(self):
        metrics = []
        dict_data = self.to_dict()
        for key in dict_data:
            val = dict_data[key]
            if val is None:
                continue
            if key in ['ip', 'node']:
                continue
            mtimestamp = int(time.time())
            metric_key = '{0}.{1}.{2}'.format(self.ip.replace('.', '-'), self.node, key)

            metrics.append((metric_key, (mtimestamp, val)))

        return metrics

    @staticmethod
    def from_dict(dict_data):
        ip = dict_data.get('ip', None)
        node = dict_data.get('node', None)
        conns = dict_data.get('conns', None)
        conns_max = dict_data.get('conns-max', None)

        return Business(ip=ip, node=node, conns=conns, conns_max=conns_max)

    @staticmethod
    def from_json(json_data):
        dict_data = json_data.loads(json_data)

        return Business.from_dict(dict_data)


class Mcombine(object):
    def __init__(self, basics=None, business=None):
        self.basics = basics
        self.business = business

    @property
    def basics_metrics(self):
        metrics = {}
        metrics_list = []

        for item in self.basics:
            pair_list = item.to_metrics()
            if not pair_list:
                return metrics_list
            for pair in pair_list:
                mkey, mval = pair
                metrics.setdefault(mkey, [])
                metrics[mkey].append(mval[-1])

        for k in metrics:
            g_key, glist = k, metrics[k]
            g_val = sum(glist)/len(glist)
            metrics_list.append((g_key, (int(time.time()), g_val)))

        return metrics_list

    @property
    def business_metrics(self):
        metrics = {}
        metrics_list = []

        for item in self.business:
            pair_list = item.to_metrics()
            if not pair_list:
                return metrics_list
            for pair in pair_list:
                mkey, mval = pair
                metrics.setdefault(mkey, [])
                metrics[mkey].append(mval[-1])

        for k in metrics:
            g_key, glist = k, metrics[k]
            g_val = sum(glist)
            metrics_list.append((g_key, (int(time.time()), g_val)))

        return metrics_list


@register_as_handler(name='xmcloud3_service_jsonrpc')
class Xmcloud3ServiceJsonRpc(object):
    _ins = None

    def __init__(self, *args, **kwargs):
        self.debug = kwargs.get('debug', False)

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Xmcloud3ServiceJsonRpc, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def filter_data(self, data):
        if self.debug:
            fmtdata = (self.__class__.__name__, self.filter_data.__name__, data)
            msgdata = 'filter-{0}-handler-{1} got data, data={2}'.format(*fmtdata)
            logging.debug(msgdata)

        input_mark, input_data, mbasics, mbusiness = data['mark'], data['data'], [], []
        for item in input_data['result']:
            mbasics.append(Basics.from_dict(item))
            mbusiness.append(Business.from_dict(item))
        mins = Mcombine(basics=mbasics, business=mbusiness)

        metrics = []
        metrics.extend(mins.basics_metrics)
        metrics.extend(mins.business_metrics)

        output_data = {
            'mark': input_mark,
            'data': metrics
        }

        return output_data






