#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.options import define

define("debug", True, help='enable debug mode')
define("port", 8990, help='run on this prot', type=int)