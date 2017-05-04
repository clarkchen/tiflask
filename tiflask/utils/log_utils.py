# -*- coding:utf-8 -*-
import logstash

from .server_utils import local_ip

__author__ = 'clarkchen'
import logging, logging.handlers
import os

log_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = "{0}/../logs".format(log_dir)

# print (log_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def log_format():
    # 默认输出到屏幕
    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=format)
    # 设定日志格式
    # 2015-06-04 16:12:56,510 - root - WARNING - fail to get taobao local name
    log_formatter = logging.Formatter(format)
    # 设定日志存留时间 7*24，保留一个星期日志，每小时为一个文件
    handler = logging.handlers.TimedRotatingFileHandler('{0}/time.log'.format(log_dir),
                                                        when='H',
                                                        interval=1,
                                                        backupCount=7 * 24)
    # 设定日志文件名格式, 这个地方和系统的不相符合，注释掉了不用了，否则不会自己删除
    # time.log.20150604-1646.log
    # handler.suffix = "%Y%m%d_%H%M.log"
    # 设定日志等级
    # 详细参数参见 https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook
    handler.setLevel(logging.INFO)
    # 加载日志格式
    handler.setFormatter(log_formatter)
    # 为root日志logger添加处理的handler
    logging.getLogger("").addHandler(handler)
    return handler


def log_format_elk(app_name, port, ip, elk_sign="elk"):
    """
    :param app_name:  要建立索引的名称
    :param elk_sign: 需要添加的过滤关键词
    :return:
    """
    """
    获得Elastic Search的 Handler
    :return:
    """
    handler = logstash.TCPLogstashHandler(ip, port=port, version=1, message_type=app_name)
    # 添加filter,只发送error和重要信息
    handler.addFilter(ContextFilter(elk_sign))
    logging.getLogger('').addHandler(handler)
    return


class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.

    Rather than use actual contextual information, we just use random
    data in this demo.
    """

    def __init__(self, elk_sign):
        super(ContextFilter, self).__init__()
        self.elk_sign = elk_sign

    def filter(self, record):
        if self.elk_sign in record.getMessage():
            record.host = local_ip
            return True
        if record.levelname in ('ERROR', 'CRITICAL', "EMERGENCY", "ALERT"):
            record.host = local_ip
            return True
        return False
