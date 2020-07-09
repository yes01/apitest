# -*- coding: UTF-8 -*-
import traceback
import pymysql
from Common.logger import Logger
logger = Logger(logger="setSql").getlog()


class SetSql:

    def connect_database_update(self):
        connect = pymysql.Connect(
            host='8.210.102.39',
            port=31007,
            user='root',
            passwd='CrazyCube!@#',
            db='CubeAgePlatform',  # 数据库名称
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = connect.cursor()
        try:
            sql = ("UPDATE UserBindAccount SET IsBound='0'  WHERE CreatedAtUtc=(select max_time from(SELECT MAX(CreatedAtUtc) as max_time  FROM UserBindAccount)as a)")
            cursor.execute(sql)
            connect.commit()  # 统一提交
            logger.info("CubeAgePlatform数据库进行update操作【执行成功】")

        except Exception as e:  # 捕捉异常，并打印
            traceback.print_exc()
        # 关闭数据库连接
        cursor.close()
        connect.close()