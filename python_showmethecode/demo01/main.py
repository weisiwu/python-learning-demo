import os
import time
import json
import string
import random
import hashlib
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps

# python中常用的加密解密库,常用的库还有 Crypto
from cryptography.fernet import Fernet

cache_file = ".verify_code_memo"

"""
验证码: VerifyCode
1、有效期限：确定验证码的有效期，防止过期验证码被使用。
2、唯一性：确保生成的验证码在同一时间内是唯一的，避免重复使用。
3、由验证码文字生成图片
4、提高验证码复杂度: 对图片内容进行扭曲变形、噪点干扰、调整字符间距、样式、颜色随机变化等、
"""


class VerifyCode:
    code = ""
    path = ""
    time = 0
    default_config = {
        # 验证码长度
        "verify_code_len": 6,
        # 验证码字符集
        "verify_code_set": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        # 7200秒
        "verify_code_expire_time": 7200,
        "verify_code_fontsize": 50,
        "verify_code_height": 80,
        "verify_code_width": 250,
        "verify_code_save_path": None,
        "noise_level": 0.05,  # 噪点级别
    }
    meme_code = {}

    def __init__(self, uuid, config=default_config):
        input_config = config if config is not None else self.default_config
        self.config = {**self.default_config, **input_config}
        self.uuid = uuid
        self.code_set_len = len(self.config["verify_code_set"])

    def get_assets_path(self, filename=""):
        return os.path.join(os.path.dirname(__file__), filename)

    def get_current_path(self):
        return (
            self.get_assets_path()
            if not self.config["verify_code_save_path"]
            else self.config["verify_code_save_path"]
        )

    def get_random_color(self):
        color = []

        for index in range(0, 3):
            color.append(random.randint(0, 255))

        return tuple(color)

    def get_random_size(self):
        font_size = self.config["verify_code_fontsize"]

        return random.randint(int(font_size * 0.85), font_size)

    def get_memo_verify_code(self):
        try:
            cache_file_path = self.get_assets_path(cache_file)
            if not os.path.isfile(cache_file_path):
                return ""

            with open(f"{cache_file_path}", "r") as file:
                memo = json.load(file)
                start_time = memo[self.uuid]["time"]  # 生成时间

            if (
                start_time + self.config["verify_code_expire_time"]
                >= datetime.now().timestamp()
            ):
                return memo[self.uuid]
            else:
                return ""
        except KeyError as e:
            print(f"\033[91m未能读取正确缓存：\033[0m")
            print(f"\033[91m{e}\033[0m")
        except json.JSONDecodeError:
            return ""

    def clear_memo(self):
        # 清空缓存
        return

    def verify_code_draw(self):
        width = self.config["verify_code_width"]
        height = self.config["verify_code_height"]
        size = self.config["verify_code_fontsize"]

        image = Image.new("RGB", (width, height), "white")
        image_draw = ImageDraw.Draw(image)
        alpha_cover = Image.new("L", (width, height), 128)  # 128 表示半透明
        alpha_cover_draw = ImageDraw.Draw(alpha_cover)

        # 给验证码图添加背景和随机线条
        for i in range(50):
            line_color = random.randint(0, 255)  # 干扰线的颜色随机生成
            start_point = (random.randint(0, width), random.randint(0, height))
            end_point = (random.randint(0, width), random.randint(0, height))
            # 在画布上绘制干扰线
            alpha_cover_draw.line([start_point, end_point], fill=line_color, width=1)

        image.paste(alpha_cover, (0, 0), alpha_cover)

        # 向图片加验证码文字
        for index, text in enumerate(self.code):
            # 随机大小和颜色
            font_size = self.get_random_size()
            font = ImageFont.truetype(
                self.get_assets_path("./ttf/From Cartoon Blocks.ttf"),
                size=font_size,
            )
            fill_color = self.get_random_color()
            # 表示如果是第一个字，左侧间距是17，后续的依次加一个字宽
            position = (17 if index == 0 else 36 * index + 17, (height - size) / 2)
            image_draw.text(position, text, fill=fill_color, font=font)

            # 扭曲文本
            twisted_text = text
            twisted_text_image = Image.new("L", (width, height))
            draw_twisted = ImageDraw.Draw(twisted_text_image)
            draw_twisted.text(position, twisted_text, font=font, fill=255)

            # 使用滤镜来扭曲文本
            # TODO:(wsw) 没有看到扭曲效果
            twisted_text_image = twisted_text_image.transform(
                (width, height),
                Image.PERSPECTIVE,
                (1.0, 0.2, -50.0, 0.0, 1.5, -100.0, 0.0, 0.001, 1.0),
                Image.BILINEAR,
            )
            image.paste(
                ImageOps.colorize(twisted_text_image, (0, 0, 0), (255, 0, 0)), (50, 100)
            )

        # 在图片中添加噪点
        noise_level = self.config["noise_level"]
        for x in range(image.width):
            for y in range(image.height):
                if random.random() < noise_level:
                    noise_color = self.get_random_color()
                    image.putpixel((x, y), noise_color)

        # 默认保存路径
        save_path = self.get_assets_path("./output")

        # 如调用时，传入保存路径，则不使用默认路径
        if self.config["verify_code_save_path"]:
            save_path = f'{self.config["verify_code_save_path"]}'

        if not os.path.isdir(save_path):
            # makedirs 可以递归创建目录
            os.makedirs(save_path)

        self.path = f"{save_path}/{self.code}.png"
        cache_file_path = self.get_assets_path(cache_file)

        try:
            # 尝试打开文件并读取内容
            with open(cache_file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            file_content = ""

        if not file_content:
            file_content = "{}"

        try:
            json_data = json.loads(file_content)

        except json.JSONDecodeError as e:
            json_data = {}
            print(f"\033[91m缓存JSON解析错误：\033[0m")
            print(f"\033[91m{e}\033[0m")

        json_data[self.uuid] = {
            "code": self.code,
            "time": datetime.now().timestamp(),
            "path": self.path,
        }

        with open(cache_file_path, "w") as file:
            json.dump(
                json_data,
                file,
                indent=4,
            )

        try:
            image.save(self.path)
        except Exception as e:
            # 防止传入的目录不可用
            image.save(f"{self.get_assets_path(f'./output/{self.code}.png')}")
            print(f"\033[91m传入的路径不可用，错误信息如下：\033[0m")
            print(f"\033[91m{e}\033[0m")

    def verify_code_generate(self):
        code_arr = [
            self.config["verify_code_set"][random.randint(0, self.code_set_len - 1)]
            for index in range(0, self.config["verify_code_len"])
        ]
        self.code = "".join(code_arr)

        # 绘制验证码图片&&提高图片的复杂度
        self.verify_code_draw()

    # 针对特定id深处验证码，如果没有传入，则从本地缓存读取未过期的验证码返回
    def verify_code(self):
        verify_code_memo = self.get_memo_verify_code()

        if bool(verify_code_memo):
            image = Image.open(verify_code_memo["path"])
        else:
            self.verify_code_generate()
            image = Image.open(self.path)

        image.show()

        return self.code

    def get_verify_code_info(self):
        return self.meme_code[self.uuid]


"""
激活码&&验证码
激活码: ActivateCode
程序设计
激活码从本质上是加密字符串
因此设计程序程序时，当关注以下几点
1、激活码是否足够随机
    防止被恶意用户猜测到
2、激活码要保持唯一
3、激活码内部信息不可以被解析
    防止泄密
为此，我们对激活码对应的原始字段，设计包含以下信息
    1、有效期
    2、生成激活码时的时间戳
    3、2块各自独立的强随机字段，分别在头尾
    4、激活码id（由时间戳+随机字段1组合后，数字签名而来）
激活码程序通过接受以上信息，生成激活码。
并且提供解析方法，将激活信息读取出来。
同时提供可靠性校验，防止伪造激活码。

至于业务逻辑，如激活码和用户关联，是否超出激活次数。
则由业务逻辑处理，不在这里涉及
"""


class ActivateCode:
    default_config = {
        "valid_date": None,
        "timestamp": None,
    }

    def __init__(self, config=default_config):
        self.base_path = os.path.dirname(__file__)
        self.private_key_path = os.path.join(self.base_path, ".private_key")
        self.code_list_path = os.path.join(self.base_path, "./activeCodeList.txt")
        # 一共生成多少条
        self.batch_number = config["batch_number"]
        # 产品信息
        self.valid_date = config["valid_date"]
        self.timestamp = time.time()
        self.code = None  # 激活码
        self.private_key = None
        self.cipher_suite = None
        self.random_text_1 = self._generate_random_str(10)
        self.random_text_2 = self._generate_random_str(10)
        self.id = self._generate_id()

    # 为激活码实例生成属于自己的id
    def _generate_id(self):
        f"{self.random_text_1}_{self.timestamp}"
        return ""

    # 生成随机字符串
    def _generate_random_str(self, len=10):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(len))

    # 加密使用AES-256算法，需要先生成私钥，私钥将会存储在本地。以便后续使用
    def encrypt(self):
        privae_key = None
        # 尝试从本地读取秘钥，如无则生成
        with open(self.private_key_path, "rb") as file:
            privae_key = file.read()

        # 生成私钥
        if not privae_key:
            # b: 二进制方式打开
            with open(self.private_key_path, "wb") as file:
                privae_key = Fernet.generate_key()
                file.write(privae_key)

        self.private_key = privae_key
        self.cipher_suite = Fernet(privae_key)

        raw_text = json.dumps(
            {
                "valid_date": self.valid_date,
                "timestamp": self.timestamp,
                "random_text_1": self.random_text_1,
                "random_text_2": self.random_text_2,
                "id": self.id,
            }
        )
        # 进行加密
        b_code = self.cipher_suite.encrypt(raw_text.encode("utf-8"))
        self.code = hashlib.md5(string=b_code, usedforsecurity=True).hexdigest()
        print("生成的激活码是 ==============>", self.code)

        return self.code

    def encrypt_batch(self):
        # 清空文件已有内容
        with open(self.code_list_path, "w") as file:
            file.write("")

        with open(self.code_list_path, "a") as file:
            for _ in range(0, self.batch_number):
                code = self.encrypt()
                file.write(f"{code}\n")

            print(f"已完成{self.batch_number}条激活码的生成！")

        with open(self.code_list_path, "r") as file:
            file.read()

    # 检测激活码的手段: 如果激活码确实是从这里发出去的，那么就是可用的，否则都不是。
    # 换言之，保存在库里的，状态是正确的数据中存储的激活码，才是有效的
    def check_valid(self, code):
        print(f"正在解码: {code}\n")
        # 检查激活码长度
        _code = code.strip()
        if len(_code) != 32:
            return False

        characters = f"{string.digits}{string.ascii_letters}"

        # all + 列表推导，迅速过滤数组中是否有不符合条件的值
        if not all(char in characters for char in _code):
            return False

        return True


if __name__ == "__main__":
    # 验证码部分
    # print(f"TEST CASE 1 START =======================\n")
    # uuid = "test_1"
    # code = VerifyCode(uuid).verify_code()
    # print(f"为{uuid}生成的验证码为: {code}\n")
    # print(f"TEST CASE 1 END =======================\n")

    # print(f"TEST CASE 2 START =======================\n")
    # uuid = "test_2"
    # code = VerifyCode(
    #     uuid, config={"verify_code_save_path": f"{os.path.dirname(__file__)}/{uuid}/"}
    # ).verify_code()
    # print(f"为{uuid}生成的验证码为: {code}\n")
    # print(f"TEST CASE 2 END =======================\n")

    batch_number = 200
    print(f"{batch_number}条激活码生成开始 =======================\n")
    # 生成激活码，并保存实例
    activate_ins = ActivateCode(
        config={
            "batch_number": batch_number,
            # 7200秒
            "valid_date": time.time() + 7e6 + 2e5,
        }
    )
    activate_code = activate_ins.encrypt_batch()
    print(f"{batch_number}条激活码生成结束 =======================\n")

    print(f"激活码解码: 随机取一条进行解码 =======================\n")
    random_index = random.randint(0, batch_number)
    with open(
        os.path.join(os.path.dirname(__file__), "./activeCodeList.txt"), "r"
    ) as file:
        for _ in range(0, batch_number):
            code = file.readline(batch_number)
            if _ == random_index:
                # 随机取一条，开始解码
                if activate_ins.check_valid(code):
                    print("\033[92m通过规则校验！\033[0m")
                else:
                    print("\033[91m未通过规则校验！\033[0m")
