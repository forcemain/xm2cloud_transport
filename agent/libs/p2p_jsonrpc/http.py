#! -*- coding: utf-8 -*-


from agent.libs.simple_http_parser.http import HttpStream
from agent.libs.simple_http_parser.reader import SocketReader


def pack_post_data(uri, **kwargs):
    header_list = []
    for item in kwargs['headers'].iteritems():
        header_list.append('{0}: {1}'.format(item[0], item[1]))

    post_data = [
        '{0} {1} HTTP/1.1'.format(kwargs['method'], uri),
        '\r\n'.join(header_list),
        '\r\n{0}'.format(kwargs['body'])
    ]

    data = '\r\n'.join(post_data)

    return data


def unblock_mode_recv(sock, buffer_size=4096):
    r = SocketReader(sock)
    s = HttpStream(r)
    s.read(buffer_size=buffer_size)
    data = s.body.next()

    return data
