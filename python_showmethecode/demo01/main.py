import os
import random
from datetime import datetime
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

"""
验证码: VerifyCode
1、有效期限：确定验证码的有效期，防止过期验证码被使用。
2、唯一性：确保生成的验证码在同一时间内是唯一的，避免重复使用。
3、由验证码文字生成图片
4、提高验证码复杂度: 对图片内容进行扭曲变形、噪点干扰、调整字符间距、样式、颜色随机变化等、
"""


# 如何写到文件中
# 如何绘制图片
class VerifyCode:
    code = ""
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
    }
    meme_code = {}

    def __init__(self, uuid, config=default_config):
        self.config = config if config is not None else self.default_config
        self.uuid = uuid
        self.code_set_len = len(self.config["verify_code_set"])

    def get_current_path(self):
        return os.path.dirname(__file__)

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
            code_memo = self.meme_code[self.uuid]["code"]
            start_time = self.meme_code[self.uuid]["time"]  # 生成时间

            if start_time + self.config["verify_code_expire_time"] >= datetime.now():
                return code_memo
            else:
                return ""
        except KeyError:
            return ""

    def verify_code_draw(self):
        width = self.config["verify_code_width"]
        height = self.config["verify_code_height"]
        size = self.config["verify_code_fontsize"]

        image = Image.new("RGB", (width, height), "white")

        image_draw = ImageDraw.Draw(image)

        for index, text in enumerate(self.code):
            # 随机大小和颜色
            font_size = self.get_random_size()
            font = ImageFont.truetype(
                f"{self.get_current_path()}/ttf/From Cartoon Blocks.ttf", size=font_size
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

        save_path = f"{self.get_current_path()}/output"

        # 如果调用的时候，传入了保存路径，则不使用默认路径
        if self.config["verify_code_save_path"]:
            save_path = self.config["verify_code_save_path"]
        elif not os.path.isdir(save_path):
            # makedirs 可以递归创建目录
            os.makedirs(save_path)

        try:
            image.save(f"{save_path}/{self.code}.png")
        except Exception as e:
            # 防止传入的目录不可用
            image.save(f"{self.get_current_path()}/output.png")
            print(f"\033[91m传入的路径（verify_code_save_path）不可用，错误信息如下：\033[0m")
            print(f"\033[91m{e}\033[0m")

        image.show()

    def verify_code_generate(self):
        code_arr = [
            self.config["verify_code_set"][random.randint(0, self.code_set_len - 1)]
            for index in range(0, self.config["verify_code_len"])
        ]
        self.code = "".join(code_arr)

        # 绘制验证码图片&&提高图片的复杂度
        self.verify_code_draw()

        self.meme_code[self.uuid] = {
            "time": datetime.now().timestamp(),
            "code": self.code,
        }

    # 针对特定id深处验证码，如果没有传入，则从本地缓存读取未过期的验证码返回
    def verify_code(self):
        if self.uuid:
            verify_code_memo = self.get_memo_verify_code()
            if not verify_code_memo:
                self.verify_code_generate()
        else:
            self.verify_code_generate()

        return self.code

    def get_verify_code_info(self):
        return self.meme_code[self.uuid]


"""
激活码&&验证码
激活码: ActivateCode
"""

if __name__ == "__main__":
    print(f"TEST CASE 1 START =======================\n")
    uuid = "test_1"
    code = VerifyCode(uuid).verify_code()
    print(f"为{uuid}生成的验证码为: {code}\n")
    print(f"TEST CASE 1 END =======================\n")
