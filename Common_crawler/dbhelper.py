# import MySQLdb
import pymysql
from scrapy.utils.project import get_project_settings

class DBHelper():
    
    def __init__(self):
        '''
        配置在config.py中的数据库信息
        '''
        self.settings=get_project_settings()
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    def connectMysql(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             charset='utf8')
        return conn
    def connectDatabase(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8')
        return conn   
    
    def createDatabase(self):
        conn=self.connectMysql()
        
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    def insert(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        

class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
               
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 
    def testCreateTable(self):
        # sql="create table testtable(id int primary key auto_increment,name varchar(50),url varchar(200))"
        sql = "CREATE TABLE `zbp_post` (`log_ID` int(11) NOT NULL AUTO_INCREMENT,`log_Title` varchar(255) NOT NULL DEFAULT '',`log_Intro` text NOT NULL,`log_Content` longtext NOT NULL,)) ENGINE=MyISAM AUTO_INCREMENT=600 DEFAULT CHARSET=utf8;"
        self.dbHelper.createTable(sql)
    def testInsert(self):
        # sql="insert into testtable(name,url) values(%s,%s)"
        sql="insert into zbp_post (log_Title,log_Intro,log_Content) values (%s,%s,%s)"
        params=("test","test")
    def testUpdate(self):
        sql="update zbp_post set log_Title=%s,log_Content=%s where id=%s"
        params=("update","update","1")
        self.dbHelper.update(sql,*params)
    
    def testDelete(self):
        sql="delete from zbp_post where id=%s"
        params=("1")
        self.dbHelper.delete(sql,*params)
    
if __name__=="__main__":
    testDBHelper=TestDBHelper()
