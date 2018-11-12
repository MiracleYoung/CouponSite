# /usr/bin/env python
# Created by Miracle at 9/11/18

import logging
import logging.config

from app.etc.conf import config

__all__ = ['logger']


def setup_logging(cfg=config.LOGGING_CONFIG):
    logging.config.dictConfig(cfg)
    return logging.getLogger(__file__)


logger = setup_logging()
