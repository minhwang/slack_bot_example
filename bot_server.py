# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import web

urls = ('/', 'Index')

class Index:
    def GET(self):
        return "Hello, world!"
    def POST(self):
        return "Post"

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
