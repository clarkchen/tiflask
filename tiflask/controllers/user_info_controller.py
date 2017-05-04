# -*- coding:utf-8 -*-
from tiflask.controllers.return_funcs import return_value

__author__ = 'clarkchen'

import logging
import json
from tiflask.models import ScoreModel
from tiflask.models.data_operations.user_info_collector import UserInfoCollector
from tiflask.config import server_config

import json
from flask.ext.restful import abort, Resource
import logging, datetime

from flask_restful import reqparse, marshal, marshal_with, fields

# input 参数定义
parser = reqparse.RequestParser()
parser.add_argument('phone', type=str, required=True, help='phone is missing')

# output 参数定义
features_demo = {
    "recent_3_read_article_type_num": fields.Float(attribute="recent_3_read_article_type_num", default=-1),
    "read_article_type_num": fields.Float(attribute="read_article_type_num", default=-1),
    "read_article_num": fields.Float(attribute="read_article_num", default=-1),
    "recent_3_read_article_num": fields.Float(attribute="recent_3_read_article_num", default=-1),
}

resources = {
    "score": fields.Float(attribute="score"),
    "features": fields.Nested(features_demo, attribute="features")
}


class UserInfoController(Resource):
    logger = logging.getLogger(__name__)

    def __init__(self):
        pass

    @return_value
    def post(self):
        # 返回数值的设定
        args = parser.parse_args()

        ret_value = {"score": -1, "features": {}}
        ret_code = 200
        log_dict = {}
        try:
            self.logger.info("params are {0}".format(args))

            # 接收参数
            user_phone = args['phone']
            log_dict["phone"] = user_phone
            if len(user_phone) > 30 or len(user_phone) < 3:
                self.logger.error("invlid parameter")
                ret_code = 400
                return
            # 收集信息
            user_info_collector = UserInfoCollector()
            user_info = user_info_collector.prepare_user_info(phone=user_phone)

            # 计算分数
            score_model = ScoreModel()
            ret_value = score_model.predict_score(user_info)

            ret_score = ret_value.get("score")

            log_dict.update({"ret_score": ret_score})

            logging.info("{elk_sign} user {phone} score is {score}".format(phone=user_phone, score=ret_score,
                                                                           elk_sign=server_config.elk_sign),
                         extra=log_dict)
        except Exception as e:
            self.logger.exception(e)
        finally:

            return marshal(ret_value, resources), ret_code

    def delete(self):
        abort(400, message="delete api is not available")
        self.logger.error('%s\terror\tdelete api is not available' % (datetime.now().strftime("%y-%m-%d-%H:%M:%S")))

    @return_value
    def get(self):
        demo_return = {"features": {"recent_3_read_article_num": 500.0, "recent_3_read_article_type_num": 1000.0,
                                    "read_article_num": 40000.0, "read_article_type_num": 5000.0}, "score": "1998"}
        return marshal(demo_return, resources), 200
