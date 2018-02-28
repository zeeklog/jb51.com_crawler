# -*- coding: utf-8 -*-

# 数据库配置
class mysql_config():
    '''mysql数据库配置'''
    host = '127.0.0.1'
    dbname = 'max'  # 数据库名字，请修改
    user = 'root'  # 数据库账号，请修改
    psw = '920302913'  # 数据库密码，请修改
    port = 3306  # 数据库端口，在dbhelper中使用

    # 插入到数据库的格式
    # sql = "insert into zbp_post (log_Title,log_Intro,log_Content) values (%s,%s,%s)"


