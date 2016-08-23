# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import web
import json

urls = (
    '/', 'Index',
    '/hello', 'Hello',
    '/bob', 'Bob',
    '/yummy/action', 'YummyAction'
)

class Index:
    def GET(self):
        return "Hello, world!"
    def POST(self):
        return "Post"

class Hello:
    def POST(self):
        req_data = web.input()
        a = {
            'text': 'ttt',
            'attachments': [
                {
                    'text': 'aaaaa',
                    'fallback': 'fallback',
                    'callback_id': 'callback_id',
                    'color': '#3AA3E3',
                    'attachment_type': 'default',
                    'actions': [
                        {
                            'name': 'eeee',
                            'text': 'Eeee',
                            'type': 'button',
                            'value': 'dddd'
                        }
                    ]
                }
            ]
        }
        res = {'text':'Hello, {0}'.format(req_data.user_name)}
        web.header('Content-Type', 'application/json')
        return json.dumps(a)

class Bob:
    def POST(self):
        req_data = web.input()
        a = {
            'text': req_data.text,
            'attachments': [
                {
                    'response_type': 'in_channel',
                    'text': req_data.text,
                    'fallback': 'fallback',
                    'callback_id': 'callback_id',
                    'color': '#3AA3E3',
                    'attachment_type': 'default',
                    'actions': [
                        {
                            'name': 'Join',
                            'text': 'JOIN',
                            'type': 'button',
                            'value': 'join'
                        }
                    ]
                }
            ]
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(a)

class YummyAction:
    def POST(self):
        pass

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
