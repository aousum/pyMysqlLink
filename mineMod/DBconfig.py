#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 安装PyMySQL
# sudo pip install PyMySQL
import pymysql
class mysqlInfo:
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'db': 'canYou',
        'charset': 'utf8mb4',
        # 数据库内容以字典格式输出
        # 'cursorclass':pymysql.cursors.DictCursor,
    }
    # 连接数据库
    def linkSql(self):
        # 连接数据库
        # db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="Geek_Web", charset="utf8mb4")
        db = pymysql.connect(**mysqlInfo.config)
        # cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            return (db, cursor)

        except:
            print("数据库访问失败")

    # 增
    def Insert(table,useMap,db, cursor):
        newkey=''
        newValue=''
        for key, values in useMap.items():
            if newkey=='':
                newkey=key
            else:
                newkey = newkey+','+key
            if newValue=='':
                newValue="'"+values+"'"
            else:
                newValue = newValue+",'"+values+"'"

        sql = "insert into "+table+"("+newkey+") values ("+newValue+")"
        # 执行SQL语句
        cursor.execute(sql)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        db.commit()

    # 删
    def Delect(table,whereMap,db, cursor):
        where = '1=1'
        for key, values in whereMap.items():
            where = where + " and " + key + "='" + values + "' "
        sql = "DELETE FROM "+table+" WHERE "+where
        cursor.execute(sql)
        db.commit()

    # 查
    def Select(table,whereMap,useArr,db, cursor):
        where='1=1'
        for key, values in whereMap.items():
            where = where+" and "+key+"='"+values+"' "
        resList=''
        resList = ','.join(useArr)  # 简单拼接的方法
        newArr = resList.split(',') # 用**分割字符串
        for item in newArr:
            if resList=='':
                resList=item
            else:
                resList = resList+','+item
        sql = "SELECT "+resList+" FROM " + table + " where " + where
        cursor.execute(sql)
        col = cursor.description#查询查询对应的列名
        # 获取所有记录列表
        results = cursor.fetchall()
        # results = cursor.fetchmany()
        # results = cursor.fetchone()

        return results

    # 改
    def Update(table,whereMap,useMap,db, cursor):
        where = '1=1'
        for key, values in whereMap.items():
            where = where + " and " + key + "='" + values + "' "
        changeList = ''
        for key, values in useMap.items():
            if changeList=='':
                changeList= key+"='"+values+"'"
            else:
                changeList = changeList +","+ key + "='" + values + "'"
        sql = "UPDATE "+table+" SET "+changeList+" WHERE "+where
        cursor.execute(sql)
        db.commit()

    # 关闭数据库连接
    def Close(db, cursor):
        cursor.close()
        db.close()

        # (db, cursor) = linkSql()
        # print("\n-------------数据库初始状态-------------")
        # print(Select(db, cursor))
        # Insert(db, cursor)
        # print("\n-------------数据库插入数据-------------")
        # print(Select(db, cursor))
        # Update(db, cursor)
        # print("\n-------------数据库修改数据-------------")
        # print(Select(db, cursor))
        # Delect(db, cursor)
        # print("\n-------------数据库删除数据-------------")
        # print(Select(db, cursor))
        # Close(db, cursor)