# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pymysql

class DevicesJDPipeline:
    tb = 'device_jd'
    number = 0

    def open_spider(self, spider):
        print("开始爬虫！")
        db = spider.settings.get('MYSQL_DB_NAME','cve_db')
        host = spider.settings.get('MYSQL_HOST','127.0.0.1')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER','root')
        passwd = spider.settings.get('MYSQL_PASSWORD','root')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

        # 三句话为删表重建，往数据库补充数据注释掉
        self.db_cur.execute("DROP TABLE IF EXISTS %s"%self.tb)
        sql = """CREATE TABLE IF NOT EXISTS %s (
            id int PRIMARY KEY AUTO_INCREMENT, 
            productid varchar(16),
            productname varchar(128),
            brand varchar(56),
            modlenumber varchar(64),
            producttype varchar(128)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        self.db_cur.execute(sql%self.tb)
        print('建表完成！')

    def process_item(self, item, spider):
        if item != None:
            sql = 'INSERT INTO {}(productid,productname,brand,modlenumber,producttype) VALUES("{}","{}","{}","{}","{}")'.format(self.tb,item['productid'],item['productname'],item['brand'],item['modlenumber'],item['producttype'])
            print(sql)
            self.db_cur.execute(sql)
            self.number += 1
            if self.number >= 60:
                self.db_conn.commit()
                self.number = 0
        return item

    def close_spider(self, spider):
        print("结束爬虫！")
        self.db_conn.commit()
        self.db_conn.close()
