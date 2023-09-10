import os
import time
import random
import MySQLdb
from ..demo01.main import ActivateCode

print(f"ActivateCode {ActivateCode}")


def connect_db():
    pass


def create_table():
    pass


def append_data():
    pass


if __name__ == "__main__":
    batch_number = 200
    # 生成激活码，并保存实例
    activate_ins = ActivateCode(
        config={
            "batch_number": batch_number,
            # 7200秒
            "valid_date": time.time() + 7e6 + 2e5,
        }
    )
    activate_code = activate_ins.encrypt_batch()
    random_index = random.randint(0, batch_number)

    with open(
        os.path.join("../demo01", os.path.dirname(__file__), "./activeCodeList.txt"),
        "r",
    ) as file:
        for _ in range(0, batch_number):
            print(f"code是什么 {code}")
            code = file.readline(batch_number)
            append_data(code)
