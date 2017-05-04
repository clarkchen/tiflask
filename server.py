# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__author__ = 'clarkchen'

from tiflask.app import app
from tiflask.config import server_config

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=int(server_config.port), debug=True, threaded=True)  # port is 5000 default
    except Exception as e:
        app.logger.exception(e)

# 启动脚本
# gunicorn -w4 -b0.0.0.0:5000 server:app