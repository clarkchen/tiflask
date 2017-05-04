from unittest import TestCase

import logging

from tiflask.utils.log_utils import log_format_elk, log_format
log_format()

log_format_elk("demo", elk_sign="elk", ip="alitest", port=9999 )

class TestLog_format_elk(TestCase):
    def test_log_format_elk(self):

        logger = logging.getLogger("demo")
        print ("elk test hello")
        logger.info("elk test hello")
