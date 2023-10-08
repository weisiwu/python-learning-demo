import os
import MySQLdb


class CodeTable:
    def __init__(self):
        # 必须要使用root用户
        # db 是可以不指定的，如果指定了一个不存在的db，运行会提示错误。
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Wsw51966",
        )
        self.cursor = self.db.cursor()

    def create_database(self, database):
        self.cursor.execute("show databases;")

        # 判断是否已经存在对应数据库
        databases = self.cursor.fetchall()

        for db_name in databases:
            if db_name[0] == database:
                self.cursor.execute(f"use {database};")
                return self

        # 创建数据库
        self.cursor.execute(f"CREATE DATABASE {database};")

        # 选择数据库
        self.cursor.execute(f"use {database};")

        return self

    def create_table(self, table):
        self.cursor.execute("show tables;")

        # 如果表已经存在
        tables = self.cursor.fetchall()

        for table_obj in tables:
            if table_obj[0] == table:
                return self

        # 由于是激活码，所以需要指定值唯一
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                code VARCHAR(255) UNIQUE NOT NULL
            )
            """
        )

        return self

    def insert_data(self, table, key, value):
        insert_sql = "INSERT INTO " + table + " (" + key + ") VALUES (%s)"
        # 注意，(value,)括号里面的逗号不可省略，否则插入的数据不会被视为元祖，而是作为字符串
        self.cursor.execute(
            insert_sql,
            (value,),
        )

        return self

    def commit(self):
        if self.db:
            self.db.commit()

        return self


if __name__ == "__main__":
    batch_number = 200
    database_name = "demo02"
    table_name = "activate_code"
    key = "code"

    code_db = CodeTable()
    # 选择数据库，并创建存储数据的表（如果存在则直接复用）
    code_db.create_database(database_name).create_table(table_name).commit()

    with open(
        os.path.join(os.path.dirname(__file__), "../demo01/activeCodeList.txt"),
        "r",
    ) as file:
        try:
            for _ in range(0, batch_number):
                code = file.readline(batch_number)
                code_db.insert_data(table_name, key, code)

            code_db.commit()
        except Exception as e:
            print(f"数据插入遭遇错误: {e}")
            # 发生异常时回滚事务
            code_db.db.rollback()

        # 关闭游标和数据库链接
        code_db.cursor.close()
        code_db.db.close()
