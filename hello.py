#!/usr/bin/env python
# -*- coding: utf-8 -*-


bind = '0.0.0.0:8080'

def application(environ, start_response):
    status = '200 OK'
    raw_uri = environ['RAW_URI']
    try:
        s = raw_uri[raw_uri.index('?')+1:].split('&')
        print(s)
        headers = [ ('Content-Type', 'text/plain') ]
        start_response(status, headers)
        return [bytes('\n'.join(s).encode('utf-8'))]
    except:
        return [bytes('error', 'utf-8')]
