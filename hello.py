#!/usr/bin/env python
# -*- coding: utf-8 -*-


bind = '0.0.0.0:8080'

def application(environ, start_response):
    status = '200 OK'
    #raw_uri = environ['RAW_URI']
    qstr = environ['QUERY_STRING'].split('&')
    try:
        #s = raw_uri[raw_uri.index('?')+1:].split('&')
        #print(s)
        body = [ bytes(i + '\n', 'ascii') for i in qstr ]
        headers = [ ('Content-Type', 'text/plain') ]
        start_response(status, headers)
        return body
    except BaseException as err:
        return [bytes(err.__str__(), 'ascii')]
