# -*- coding: utf-8 -


"""
1. parser socket http sticky package with content_length in Header
"""


import re


class HttpStream(object):
    __len = re.compile(r'Content-Length: (?P<n>[0-9]+)')
    __vre = re.compile(r'HTTP/(?P<p>\d+).(?P<m>\d+) (?P<n>\d{3}) (?P<s>\w+)')
    __buf = ''
    __res = []

    def __init__(self, stream):
        self.stream = stream

    def __version_match(self):
        match = re.search(self.__class__.__vre, self.__class__.__buf)

        return match

    def __content_length_match(self, header):
        match = re.search(self.__class__.__len, header)

        return match

    def __content_length_expand(self, match):
        tpl = '\g<n>'

        return match.expand(tpl)

    def __version_match_expand(self, match):
        tpl = 'HTTP/\g<p>.\g<m> \g<n> \g<s>'

        return match.expand(tpl)

    def parser(self, data):
        end_flag = '\r\n'*2

        self.__class__.__buf += data
        if data.endswith(end_flag):
            return
        match = self.__version_match()
        if not match:
            return

        match_str = self.__version_match_expand(match)
        strs_list = self.__class__.__buf.split(match_str)

        data_dpos = 0
        """
        1. 等于一个HTTP/1.1 200 OK,需要特殊处理
            1. 存在\r\n\r\n时
            2. 不存在\r\n\r\n\时
        2. 大于一个HTTP/1.1 200 OK
        """
        for item in strs_list:
            data_dpos = data_dpos + len(match_str) + 2 + len(item)
            if end_flag in item:
                header, body = item.split(end_flag)
                match = self.__content_length_match(header)
                if not match:
                    data_dpos = 0
                    continue
                content_length = int(self.__content_length_expand(match))
                if len(body.strip()) < content_length:
                    data_dpos = 0
                    continue
                self.__class__.__res.append(body[:content_length])
            else:
                data_dpos = 0

        self.__class__.__buf = self.__class__.__buf[data_dpos:]

    def read(self, buffer_size=4096):
        b = bytearray(buffer_size)
        recved = self.stream.readinto(b)
        del b[recved:]
        data = bytes(b)

        self.parser(data)

    @property
    def body(self):
        while True:
            if not self.__class__.__res:
                yield ''
            yield self.__class__.__res.pop()

