# -*- coding: utf-8 -*-
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

from server import app, PORT


if __name__ == '__main__':
    container = tornado.wsgi.WSGIContainer(app)
    http_server = tornado.httpserver.HTTPServer(container)
    print('listen at port [{0}]'.format(PORT))
    http_server.listen(PORT, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()