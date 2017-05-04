# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask.ext.restful import Api

# from tiflask.controllers import get_user_score_controller
from tiflask.controllers.user_info_controller import UserInfoController

__author__ = 'clarkchen'
from flask import Flask

from tiflask.utils import log_format, log_format_elk
from tiflask.config import server_config

app = Flask(__name__)

log_format()

log_format_elk(server_config.project_name, ip="47.93.116.230", port=9999, elk_sign=server_config.elk_sign)

api = Api(app)

api.add_resource(UserInfoController, '/api/user_score')
