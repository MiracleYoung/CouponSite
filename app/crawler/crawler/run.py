#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/12/18

__author__ = 'MiracleYoung'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from scrapy import cmdline

name = 'tb-test'
cmd = f'scrapy crawl {name}'
cmdline.execute(cmd.split())
