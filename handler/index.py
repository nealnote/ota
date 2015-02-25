#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler
from data import DATA

PACKAGE_NAME = 'com.your.package.name'

def parseData(v):
  package = PACKAGE_NAME
  ret = {
    'cate':v[0],
    'path':v[1],
    'name':v[2],
  }
  ret['desc'] = v[3] if len(v)>3 else None
  ret['package'] = v[4] if len(v)>4 else package
  return ret

class IndexHandler(BaseHandler):
  def get(self, act):
    ios, android = {}, {}
    data = DATA
    if act not in ['ios', 'android']:
      act = None
    for k,d in enumerate(data):
      v = parseData(d)
      v['_id'] = k
      cate = v.get('cate')
      path = v.get('path')
      assert cate
      assert path
      if path.endswith('.ipa'):
        if ios.has_key(cate):
          ios[cate].append(v)
        else:
          ios[cate] = [v]
      if path.endswith('.apk'):
        if android.has_key(cate):
          android[cate].append(v)
        else:
          android[cate] = [v]
    req = self.request
    # ios require https
    #link = ''.join(['https://', req.host])
    link = ''.join([req.protocol, '://', req.host])
    self.render("index.html",
      action = act,
      body_class = "index",
      ios = [(k,ios[k]) for k in sorted(ios.keys(),reverse=True)],
      android = [(k,android[k]) for k in sorted(android.keys(),reverse=True)],
      link = link,
    )

class PlistHandler(BaseHandler):
  def get(self,idx):
    data = DATA
    id = int(idx)
    app = parseData(data[id])
    # set default version 1.0 for plist
    app['cate'] = '1.0'
    req = self.request
    link = ''.join([req.protocol, '://', req.host])
    self.set_header('Content-Disposition', 'attachment; filename=manifest.plist')
    self.render("plist.html",
      body_class = "plist",
      app = app,
      id = id,
      link = link,
    )


class DplHandler(BaseHandler):
  def get(self, act):
    self.render("dpl.html",
      body_class = "dpl",
    )
