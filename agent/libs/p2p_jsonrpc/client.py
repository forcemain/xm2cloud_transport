#! -*- coding: utf-8 -*-


import json
import uuid
import time
import base64
import socket
import random
import logging
import hashlib
import logging
import threading


from Queue import Queue
from agent.libs.p2p_jsonrpc.http import pack_post_data, unblock_mode_recv


class State(object):
    nonce = None
    token = None


class Client(object):
    _ins = None
    _min = 1
    _max = pow(2, 31)

    def __init__(self, host=None, port=None, username=None, password=None, queue=None):
        # for output
        self.queue = queue

        # for nonce and token
        self.state = State
        self.username = username
        self.password = password

        # for conn json-rpc server
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # unblocking send or recv
        self.start()

    def __new__(cls, *args, **kwargs):
        cls._ins = cls._ins or super(Client, cls).__new__(cls, *args, **kwargs)

        return cls._ins

    def __randomid(self):
        request_id = random.randint(self.__class__._min, self.__class__._max)
        session_id = '{0}_{1}'.format(uuid.uuid1().hex, request_id)

        return request_id, session_id

    def __postdata(self, uri, **kwargs):
        packed_data = pack_post_data(uri, **kwargs)
        self.sock.sendall(packed_data)

    def __strs_md5(self, md5):
        hex_str_list = []
        for i in xrange(0, len(md5), 2):
            i_hex = chr(int(md5[i: i + 2], 16))
            hex_str_list.append(i_hex)

        return ''.join(hex_str_list)

    def __encpasswd(self, nonce, passwd):
        pass_str = '{0}{1}'.format(nonce, passwd)
        pass_md5 = hashlib.md5(pass_str).hexdigest()
        pass_md5 = self.__strs_md5(pass_md5)
        pass_b64 = base64.b64encode(pass_md5)

        return pass_b64

    def __validate(self, data):
        required_rsp_fields = ['id', 'method', 'result']
        is_valid = True

        for field in required_rsp_fields:
            if field not in data:
                is_valid = False
                break

        return is_valid

    def __auth_req_handler(self, data):
        fmtdata = (self.__class__.__name__, self.__auth_req_handler.__name__, data)
        logging.debug('{0}.{1} recv data, data={2}'.format(*fmtdata))

        auth_keys = ['nonce', 'token']
        data_rets = data['result']
        for key in auth_keys:
            if key not in data_rets:
                continue
            setattr(self.state, key, data_rets[key])

    def __domain_req_handler(self, data):
        fmtdata = (self.__class__.__name__, self.__domain_req_handler.__name__, data)
        logging.debug('{0}.{1} recv data, data={2}'.format(*fmtdata))

        clear_data = json.dumps(data)
        self.queue.put(clear_data)

    def __node_req_handler(self, data):
        fmtdata = (self.__class__.__name__, self.__node_req_handler.__name__, data)
        logging.debug('{0}.{1} recv data, data={2}'.format(*fmtdata))

        clear_data = json.dumps(data)
        self.queue.put(clear_data)

    def __dispatch(self, data):
        route_map = {
            'xmcloud/service/login': self.__auth_req_handler,
            'xmcloud/service/domain/stat': self.__domain_req_handler,
            'xmcloud/service/node/stat': self.__node_req_handler,
        }
        fmtdata = (self.__class__.__name__, self.__dispatch.__name__, data)
        if not self.__validate(data):
            logging.error('{0}.{1} recived invalid data, data={2}'.format(*fmtdata))
            return
        handler = route_map.get(data['method'], None)
        if handler is None:
            logging.error('{0}.{1} can not found handler, data={2}'.format(*fmtdata))
            return

        handler(data)

    def start(self):
        def target():
            while True:
                try:
                    json_data = unblock_mode_recv(self.sock)
                    dict_data = json.loads(json_data)
                except (socket.error, TypeError, ValueError):
                    """
                    socket.error, maybe connect is closed
                    TypeError, maybe json type error
                    ValueError, maybe not json
                    
                    ignore, continue
                    """
                    time.sleep(1)
                    continue

                self.__dispatch(dict_data)
        t = threading.Thread(target=target)
        t.setDaemon(True)
        t.start()

    def auth_nonce(self):
        method = 'xmcloud/service/login'
        uri = '/{0}'.format(method)
        request_id, session_id = self.__randomid()

        body = {
            'id': request_id,
            'jsonrpc': '2.0',
            'method': method,
            'params': {'username': self.username}
        }
        js_body = json.dumps(body)
        headers = {
            'Host': '{0}:{1}'.format(self.host, self.port),
            'Accept': '*/*',
            'Connection': 'Keep-alive',
            'charsets': 'utf-8',
            'Content-Type': 'application/json',
            'Content-Length': len(js_body),
        }

        self.__postdata(uri, method='POST', headers=headers, body=js_body)

    def auth_login(self):
        method = 'xmcloud/service/login'
        uri = '/{0}'.format(method)
        request_id, session_id = self.__randomid()
        password_enc = self.__encpasswd(self.state.nonce, self.password)

        body = {
            'id': request_id,
            'jsonrpc': '2.0',
            'method': method,
            'params': {
                'username': self.username,
                'password': password_enc
            }
        }
        js_body = json.dumps(body)
        headers = {
            'Host': '{0}:{1}'.format(self.host, self.port),
            'Accept': '*/*',
            'Connection': 'Keep-alive',
            'charsets': 'utf-8',
            'Content-Type': 'application/json',
            'Content-Length': len(js_body),
        }

        self.__postdata(uri, method='POST', headers=headers, body=js_body)

    def query(self, method=None, params=None):
        uri = '/{0}'.format(method)
        request_id, session_id = self.__randomid()

        body = {
            'id': request_id,
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'token': self.state.token
        }
        js_body = json.dumps(body)
        headers = {
            'Host': '{0}:{1}'.format(self.host, self.port),
            'Accept': '*/*',
            'Connection': 'Keep-alive',
            'charsets': 'utf-8',
            'Content-Type': 'application/json',
            'Content-Length': len(js_body),
        }

        self.__postdata(uri, method='POST', headers=headers, body=js_body)
