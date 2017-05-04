# tiflask 框架
  
##  代码场景

  用户场景，查询 用户 关注的新闻, 日志登录信息，以及付费信息
  输入 电话号码，
  输出 用户的姓名，年龄，所在公司（MySQL），关注的文章的标题和内容(Article)
  登录日志信息以及付费信息
  涉及MySQL, Mongo的数据库操作


## 代码包说明

tiflask 项目包

* app.py Flask app 对象初始化的文件
    
* controllers 控制层的代码，根据指定的路由规则，处理不同的输入参数，调用对应的 model 层代码
    
* models 模型层代码，主要是根据输入数据，进行数据库操作和进一步的加工处理，给出返回值到 调用的 Controller 层

* dao 数据访问层，将数据访问的操作封装在这里，最理想的情况，model 层没有SQL语句出现
    
* objects 模型映射代码，主要是根据传入的Dict对象，进行加工处理返回一个实体对象，数据来源可以是 Mongo, Mysql 或者是 HTTP 请求
    
* dbhelper 数据库操作代码，分为 MySQL 和 Mongo 两种进行封装，只封装进行最简单的操作，由dao层调用，注意Mongo 和 MySQL 的数据库连接最好都是 连接池的形式。
    PyMongo自带连接池功能，而MySQL则需要通过 dataset(SQLalchemy) 才会有连接池功能
    
* utils 工具包，主要放一些不依赖于数据库，不依赖于业务的一些工具类，例如 身份证操作类，编码操作类

* test 单元测试代码包，右键运行 “Unit Tests in Test” 就能自动运行，test 包中的所有测试代码，里面的各个代码主要是在代码写好之后，写的测试用例，保证代码的基本情况可用

* run.sh 通过 gunicorn 的方式来启动


## 新功能开发流程

   如果要开发一个新的功能，请按照以下建议步骤来做，
   
   重要的事情说三遍，***先从Dao层开始***，***先从Dao层开始***，***先从Dao层开始***，***Git每天提交***，***Git每天提交***，***Git每天提交***
   
   * 前置：建立Git代码库，在完成重要功能或者结束一天工作之后，提交代码，写好注释，最好每天都有提交
   
   * 确认自己开发项目相关的数据库，以及查询量（避免傻逼操作），配置开发库和生产库
   
   * 编写 dao层 中 对应数据库的数据对象的代码，例如 dao/*.py 中的程序代码  
   
   * 然后针对Dao层中的返回的数据构建Objects层的内容
   
   * 添加测试用例test/object_stories/*.py 中的测试代码
   
   * 写实现业务的 model 层，并且对关键逻辑添加单元测试, 例如 models/user_info.py 
   
   * 指定对应的请求处理的controller，并且将 model 添加进入 controller 的处理流程，例如 controllers/user_info_controller.py
   
   * 编写一个调用对应接口的单元测试，检查其是否能够顺利运行，例如 test/services/test_service.py
   
   * 如果有新添加的工具类，添加到utils文件夹
   
   * 补充测试用例，运行其他所有的测试用例，看是否能够运行
   
   * 大量调用接口进行压力测试，看是否会报错
   
   * 将本地环境导出到 requirements.txt , `pip freeze > requirements.txt`
    
   * 上传Git的Mastfe分支，标记版本（打Tag），完善 readme 文档，打分逻辑除了借口文档还要写逻辑文档
  
  