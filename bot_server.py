# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import web
import json

urls = (
    '/', 'Index',
    '/hello', 'Hello'
)

class Index:
    def GET(self):
        return "Hello, world!"
    def POST(self):
        return "Post"

class Hello:
    def POST(self):
        req_data = json.loads(web.data())
        res = {'text':'Hello, {0}'.format(req_data['user_name'])}
        return json.dumps(res)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
