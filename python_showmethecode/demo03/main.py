import os
import redis

"""
向redis存储001题中生成的100条激活码数据，并读取展示
"""
if __name__ == "__main__":
    batch_number = 200
    prefix_name = "activate_code"
    field = "code"

    with open(
        os.path.join(os.path.dirname(__file__), "../demo01/activeCodeList.txt"),
        "r",
    ) as file:
        try:
            r = redis.Redis(host="localhost", port=6379, db=0)
            key_exissted = []

            for _ in range(0, batch_number):
                name = f"{prefix_name}_{_}"

                # 判断是否存在
                name_exists = r.exists(name)

                if name_exists:
                    key_exissted.append(_)
                    print(f"({_ + 1})数据已存在 => " + r.hget(name, field).decode("utf-8"))
                    continue

                # 写数据
                code = file.readline(batch_number)
                r.hset(name, field, code)

                # 读数据
                print(
                    f"向({_ + 1})写入数据 => "
                    + r.hget(f"{prefix_name}_{_}", field).decode("utf-8")
                )

        except Exception as e:
            print(f"数据插入遭遇错误: {e}")
            # 发生异常时回滚事务
