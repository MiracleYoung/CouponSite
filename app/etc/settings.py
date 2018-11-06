#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/6/18

__author__ = 'MiracleYoung'

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'log')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s : %(message)s'
        },
        'simple': {
            'format': '%(asctime)s - %(levelname)s : %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
        },
        'file_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'coupon-site.log'),
            #        suffix: "%Y%m%d_%H%M%S.log"
            'when': 'D',
            'interval': 7,
            'backupCount': 4,
            'encoding': 'utf8'
        },
        'error_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 104857600,  # 10MB
            'backupCount': 20,
            'encoding': 'utf8',
        }

    },
    'loggers': {
        'coupon_handler': {
            'handlers': ['console', 'file_handler', 'error_file_handler'],
            'level': 'INFO',
            'propagate': True
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file_handler'],
    }
}

if __name__ == '__main__':
    print(BASE_DIR)
