import os
from MySQLdb import _mysql


class CodeTable:
    def __init__(self):
        self.db = _mysql.connect(
            host="localhost",
            user="root",
        )
        self.cursor = self.db.cursor()

    def create_database(self, database):
        database_query_result = self.cursor.execute("show databases;")
        print(f"database_query_result {database_query_result}")

        # 创建数据库
        create_database_result = self.cursor.execute(f"CREATE DATABASE {database};")
        print(f"create_database_result {create_database_result}")

        # 选择数据库
        self.cursor.execute("use demo02;")
        self.db.commit()

        return self

    def create_table(self, table):
        table_query_result = self.cursor.execute("show tables;")

        create_table_result = self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                code VARCHAR(255) NOT NULL
            )
            """
        )

        self.db.commit()

        return self

    def insert_data(self, code):
        database_query_result = self.cursor.execute(
            """
            INSERT INTO users (code)
            VALUES (%s)
            """,
            (code),
        )
        self.db.commit()

        return self


if __name__ == "__main__":
    batch_number = 200

    code_db = CodeTable()
    code_db.create_database("demo02").create_table("activate_code")

    # with open(
    #     os.path.join(os.path.dirname(__file__), "../demo01/activeCodeList.txt"),
    #     "r",
    # ) as file:
    #     for _ in range(0, batch_number):
    #         # print(f"code是什么 {code}")
    #         code = file.readline(batch_number)
    #         append_data(code)
