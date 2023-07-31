##-*-coding: utf-8-*-

# 引入生成激活码的算法
from activeCode import generate_code
import pymysql

activeArr = generate_code()

# 打开连接
db = pymysql.connect()

# 获取游标
cursor = db.cursor()

for activeCodeItem in activeArr: 
  sql = "Insert into activecode(code) \
    values (%s)" % (activeCodeItem)
  try:
    # 执行插入
    cursor.execute(sql)
    db.commit()
  except:
    db.rollback()

# 全部结束关闭数据库
db.close()