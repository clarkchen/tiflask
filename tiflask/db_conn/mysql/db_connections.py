# -*- coding:utf-8 -*-
from tiflask.config import *

import dataset

def dataset_sql_connection(mysql_config, db_name=None):
    """
    利用datacenter线程池的特性
    :param mysql_config:
    :param db_name:
    :return:
    """
    mysql_db = mysql_config.db_name if db_name is None else db_name
    password = mysql_config.passwd
    host = mysql_config.host
    user = mysql_config.user
    url = "mysql://{db_user}:{db_passwd}@{db_host}/{db_name}?charset=utf8".format(db_user =user, db_passwd=password, db_host=host, db_name = mysql_db )
    ret = dataset.connect(url,reflect_metadata=False, reflect_views=False, engine_kwargs={"pool_size":20, "max_overflow":300, "pool_recycle": 3600 },)
    return ret

user_db = dataset_sql_connection(mysql_user_config)

