#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/29/18

__author__ = 'MiracleYoung'


class CouponException(Exception):
    pass


class CrawlerException(CouponException):
    pass


class SiteException(CouponException):
    pass
