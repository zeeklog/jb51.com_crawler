python3.6 + mysql爬取脚本之家文章
=======



       @@@@@                                                         @@@@@                          *@*
     =@@@@@@                                                       ~@@@@@@                          *@*
    .@@!   ,                                                       @@=   .                          *@*
    @@@       .@@@@   @@ @@@ ,@@@  :@@#@@! @@@    @@@@~   @@!@@@  @@@      $@#@@ -@@@@  @@.  @@  @@ *@*   @@@=  @@~@@
    @@       -@@@@@@  @@@@@@@@@@@: :@@@@@@@@@@@  @@@@@@!  @@@@@@  @@       $@@@@ #@~#@@ ;@@ .@@  @@ *@*  @@-@@! @@@@@
    @@       @@   @@# @@;  @@  *@@ :@@  @@,  @@ *@@   @@  @@  @@* @@       $@@       @@  @@ @@@= @@ *@* @@   @@ @@@
    @@       @@   -@@ @@   @@  -@@ :@@  @@   @@ @@:   @@  @@  @@= @@       $@#   ,@@@@@  @@ @:@@ @, *@* @@@@@@@ @@~
    @@@      @@   ;@@ @@   @@  -@@ :@@  @@   @@ @@$   @@  @@  @@= @@@      $@#   @@  @@  @@ @ @@*@  *@* @@..... @@~
    ,@@@  ,@ @@$  @@. @@   @@  -@@ :@@  @@   @@ .@@  *@@  @@  @@=  @@@  .@ $@#   @@  @@   @*@ ~@@@  *@* @@*     @@~
     =@@@@@@  @@@@@@  @@   @@  -@@ :@@  @@   @@  @@@@@@   @@  @@=  :@@@@@@ $@#   @@@@@@   @@@  @@*  *@*  @@@@@  @@~
       :@@:    ~@@    ,,   ,,   ,, .,,  ,,   ,,    @@-    ,,  ,,.    ~@@;  .,,    @@ ,,   ,,   ,,   .,.   :@@.  ,,




##### [介绍文档]
<<<<<<< HEAD

    * python版本：python3.6
    * scrapy: 1.5.0
    * 需要安装pymysql包支持访问mysql数据库
    * 可以使用pip安装： pip install pymysql
    # 重要提示

```
    或者按照下述方法执行一键安装依赖：pip install -r requirements.txt
    重要事情说三遍：请确保你安装了mysql数据库！ 请确保你安装了mysql数据库！ 请确保你安装了mysql数据库！
=======
'''
    python版本：python3.6
    scrapy: 1.5.0
    需要安装pymysql包支持访问mysql数据库
    可以使用pip安装： pip install pymysql'''

# 重要提示
    *或者按照下述方法执行一键安装依赖：pip install -r requirements.txt
    
    *重要事情说三遍：请确保你安装了mysql数据库！ 请确保你安装了mysql数据库！ 请确保你安装了mysql数据库！
    
>>>>>>> c94e53c914e600688df6942660994bf419715666

    *所有平台的Mysql下载地址为： https://dev.mysql.com/downloads/
    挑选你需要的 MySQL Community Server 版本及对应的平台。
<<<<<<< HEAD
```
=======

>>>>>>> c94e53c914e600688df6942660994bf419715666

### 爬虫工作配置

* 第一步：下载github项目文件

```shell
git clone git@github.com:caffreycc/jb51.com_crawler.git

或者直接到https://github.com/caffreycc/jb51.com_crawler.git 下载zip文件
```

* 第二步：安装依赖:

```shell
pip install -r requirements.txt
```

* 第三步：修改配置Config.py:

```shell
# Config.ini 为项目配置文件 【数据库使用mysql数据库】
    host = '127.0.0.1' #本地地址
    dbname = 'max'  # 数据库名字，请修改
    user = 'root'  # 数据库账号，请修改
    psw = '920302913'  # 数据库密码，请修改
    port = 3306  # 数据库端口，在dbhelper中使用

### 问题反馈

　　有任何关于项目的问题欢迎提issues

### 贡献代码

    本项目基于PythonCrawler-Scrapy-Mysql-File-Template开发，感谢作者@lawlite19（https://github.com/lawlite19）的开源分享精神。

