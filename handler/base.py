#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime

import tornado.web
import tornado.gen

from tornado.options import options

class BaseHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
    if options.debug:
      self.set_header("Access-Control-Allow-Origin", "*")
      self.set_header('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS')

  def redirect_by_referer(self):
    redirect = self.request.headers.get('Referer', '/')
    self.redirect(redirect)

  def _json(self, data):
    def type_handler(obj):
      if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.isoformat()
      #elif isinstance(obj, ObjectId):
        #return str(obj)
      else:
        return obj
    return json.dumps(data, default=type_handler)

  def jsondump(self, data):
    self.write(self._json(data))
