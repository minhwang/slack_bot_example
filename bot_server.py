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
            'text': '생일 축하 파티',
            'attachments': [
                {
                    'text': '생일축하합니다~ 밥 먹으러 갑시다~~',
                    'fallback': 'fallback',
                    'callback_id': 'callback_id',
                    'color': '#3AA3E3',
                    'attachment_type': 'default',
                    'actions': [
                        {
                            'name': 'Join',
                            'text': '당근 가야지~',
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
        
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
