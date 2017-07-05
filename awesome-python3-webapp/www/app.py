# -*- coding:utf-8 -*-
"""
 web app
"""
import logging;logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Awsome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # app.router.add_route('GET', '/hello/', hello)
    # app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()