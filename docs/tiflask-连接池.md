# 数据库访问连接池修改

## 1. 概述
Flask 框架可以配置为多线程访问，所以支持MySQL 和 Mongo的线程池访问

性能测试效果，50+倍的处理量提升

代码层面主要是针对 数据连接方式（dbheper） 和数据访问层（dao）的修改
最后实施的时候对于 wesync 需要更新下最新版本

## 2. 代码修改-MySQL
需要从 tornadb 转化为 SQLAlchemy，这里使用的是 SQLAlchemy的一个封装类 dataset
安装方式：`pip install dataset`


### 2.1 dbhelper 中的连接对象（变为全局线程池）

``` python
import dataset
def dataset_sql_connection(mysql_config, db_name=None):
    mysql_db = mysql_config.db_name if db_name is None else db_name
    password = mysql_config.passwd
    host = mysql_config.host
    user = mysql_config.user
    url = "mysql://{db_user}:{db_passwd}@{db_host}/{db_name}?charset=utf8".format(db_user =user, db_passwd=password, db_host=host, db_name = mysql_db )
    ret = dataset.connect(url, engine_kwargs={"pool_size":20, "max_overflow":300, "pool_recycle": 3600 },)
    return ret

user_db = dataset_sql_connection(mysql_user_config)

```




### 2.2 封装的执行类MySQLHelper

  可以直接复制tiflask 中的代码

### 2.3 dao 中的带参数的访问

 之前的访问模式：


 ```python
# 不需要Key的参数传递
sql_1 = "select * from mcc_customer where id  = %s"

# 需要Key的参数传递
sql_2 = "select * from mcc_customer where id  = %(cid)s"

helper = MySqlHelper(mobile_db)
cid = "123123"
# 第一种参数传递方式
helper.query(sql_1, cid)

# 第二种参数传递方式
helper.query(sql_1, cid=cid)

 ```

新的访问模式，必须要带Key, 参数形式变为 `:cid`
 ```python
# 需要Key的参数传递
sql_1 = "select * from mcc_customer where id  = :cid"

helper = MySqlHelper(mobile_db)
cid = "123123"

# 执行查询
helper.query(sql_1, cid=cid)

 ```


## 3. 代码修改-Mongo
### 3.1 dbhelper 中的连接方式
修改点，之前全局单例一个 client，现在单例为一个 client 和 db

修改 tiflask/dbhelper/mongo/mongo_configuation.py 中的
```python
def _init_client(mongo_config, **kwargs):
    """
    初始化 Mongo Client 全局针对一个db只需要生成一次就行
    每个 MongoClient 自带线程池
    :return:
    """
    client = MongoClient(mongo_config.mongodb_address, **kwargs)
    db = getattr(client, mongo_config.db_name)
    db.authenticate(mongo_config.user, mongo_config.passwd)
    db_name = mongo_config.db_name
    return client, getattr(client, db_name)

client_to_mongo, article_db = _init_client(mongo_article_config, **common_settings)

def get_collection(db, collection_name):
    """
    初始化到某一个具体的 Collection，需要每次动态调用
    :param collection_name: 需要用户自己来指定
    :return:
    """
    return getattr(db, collection_name)

```


### 3.2 dao 中的 collection获取方式
修改 tiflask/dao/mongo/article_info_dao.py 中的 colleciton 获取方式，直接动态获取

之前的方式
```python
 def get_article_collection(self):
      if self.article_collection is None:
          self.article_collection = get_collection(client_to_mongo, article_db_name, "demo_articles")
      return self.article_collection
```


修改之后的方式
```python
 def get_article_collection(self):
    return get_collection(article_db, "demo_articles")
```



## 4. 启动方式修改
### 4.1 修改Server.py（单机启动）

  app的run函数调用的时候增加 threaded参数

  `app.run(host='0.0.0.0', port=5000, threaded=True)`


### 4.2 用最新的wesync（服务器上线）
  gunicorn的启动方式，增加了多线程的支持
  例如 从原来的

   `gunicorn -w4 -b0.0.0.0:5000 server:app`
   变为了

    `gunicorn -w4 -b0.0.0.0:5000 --threads 20 server:app`
