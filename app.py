#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import options, parse_config_file, parse_command_line


logger = logging.getLogger('app')

# parse config
parse_config_file(os.path.join(os.path.dirname(__file__), "setting.py"))
parse_command_line()


class Application(tornado.web.Application):
  def __init__(self):
    settings = {
      'debug': options.debug,
      'gzip': True,
      'template_path': os.path.join(os.path.dirname(__file__), 'tpl'),
      'static_path': os.path.join(os.path.dirname(__file__), 'static'),
      'cookie_secret': '__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
      'xsrf_cookies': True,
      'autoreload': True
    }
    URLS = [
      (r'/dpl(.*)?', 'handler.index.DplHandler'),
      (r'/plist/([0-9]+)', 'handler.index.PlistHandler'),
      (r"/(apple-touch-icon?\.png)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
      (r'/(.*)?', 'handler.index.IndexHandler'),
    ]
    tornado.web.Application.__init__(self, URLS, **settings)

if __name__ == '__main__':
  logger.info('run at http://127.0.0.1:%r/'% options.port)
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
