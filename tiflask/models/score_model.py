# -*- coding:utf-8 -*-
__author__ = 'clarkchen'

import logging
from tiflask.models.features import FeatureGenerator
from tiflask.models.credit_model import CreditModel
from tiflask.objects import UserInfo


class ScoreModel(object):
    def __init__(self ):
        self.logger = logging.getLogger(type(self).__name__)


    def predict_score(self, user_info):
        """
        返回用户的阅读的分数
        :param user_info:
        :return:
        """
        assert isinstance(user_info, UserInfo)

        feature_generator = FeatureGenerator()
        features = feature_generator.get_features(user_info)
        self.logger.info(" feature len is {len}".format(len=len(features)))

        credit_model = CreditModel()
        score = credit_model.cal_score(user_info=user_info, features=features)
        self.logger.info("cal score is {score}, user is {uid}".format(score=score, uid=user_info.id))

        ret = {"score": score, "features": features}

        return ret