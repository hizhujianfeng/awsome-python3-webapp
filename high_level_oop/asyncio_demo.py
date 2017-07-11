# -*-coding:utf-8 -*-
"""
异步IO 消息循环， 协程EventLoop
"""
import asyncio,threading,random


# @asyncio.coroutine
# def hello():
#     print("hello, world! (%s)" % threading.current_thread())
#     # 协程，停下来执行这个的同时，进行下一个循环
#     r = yield from asyncio.sleep(1)
#     print("hello, again (%s)" % threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost:%s \r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         yield from asyncio.sleep(random.random())
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# python3.5后的语法替换
#     把@asyncio.coroutine替换为async；
#     把yield from替换为await。
# async def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     header = 'GET / HTTP/1.0\r\nHost:%s \r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         await asyncio.sleep(random.random())
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    print(type(request.match_info))
    if 'name' in request.match_info:
        text = '<h1>hello, %s!</h1>' % request.match_info['name']
    else:
        text = '<h1>hello</h1>'
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/', hello)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()