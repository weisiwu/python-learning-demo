##-*-coding: utf-8-*-\
import os
import pymysql

# 本机mysql在 /usr/local/mysql/bin/mysql 
# 登录请使用命令: /usr/local/mysql/bin/mysql -uroot -pwsw51966
# database: py_test
# table: py_activity_code
# 创建table命令
  # create table py_activity_code(
  #   code_id int auto_increment,
  #   code varchar(32),
  #   primary key(code_id)
  # ) engine=innoDB default charset=utf8;

# 读取激活码,返回数组
def read_codes():
  read_file=open(file=os.path.abspath('.')+"/demo01/activeCode.txt", mode='r')
  get_line = read_file.read()
  result = get_line.split('\n')

  return result

# 将激活码写到数据库
def write_db():
  db=pymysql.connect(host = 'localhost', password='wsw51966', user='root', charset='utf8')
  cursor=db.cursor()
  cursor.execute('use py_test;')
  codes_arr=read_codes()
  for code in codes_arr:
    cursor.execute("insert into py_activity_code (code) values ('"+code+"');")
  db.commit()

  cursor.execute('select * from py_activity_code')
  all_codes=cursor.fetchall()
  for code_record in all_codes:
    [key,record]=code_record
    if (record):
      print('---------- 读取第'+str(key)+'数据记录: '+record)
  
  cursor.close()
  db.close()

write_db()