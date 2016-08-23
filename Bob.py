# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import web
import json

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
