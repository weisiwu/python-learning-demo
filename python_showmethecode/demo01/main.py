import os
import json
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps

cache_file = ".verify_code_memo"

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

    def get_assets_path(self):
        return os.path.dirname(__file__)

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
            cache_file_path = f"{self.get_current_path()}/{cache_file}"
            if not os.path.isfile(cache_file_path):
                return ""

            with open(f"{self.get_current_path()}/{cache_file}", "r") as file:
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
                f"{self.get_assets_path()}/ttf/From Cartoon Blocks.ttf", size=font_size
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

        # 默认保存路径
        save_path = f"{self.get_assets_path()}/output"

        # 如调用时，传入保存路径，则不使用默认路径
        if self.config["verify_code_save_path"]:
            save_path = f'{self.config["verify_code_save_path"]}'

        if not os.path.isdir(save_path):
            # makedirs 可以递归创建目录
            os.makedirs(save_path)

        self.path = f"{save_path}/{self.code}.png"

        # 不能以A模式打开文件，并希望能将所有内容都读取出来
        with open(f"{self.get_assets_path()}/{cache_file}", "a") as file:
            json.dump(
                {
                    self.uuid: {
                        "code": self.code,
                        "time": datetime.now().timestamp(),
                        "path": self.path,
                    }
                },
                file,
            )

        try:
            image.save(self.path)
        except Exception as e:
            # 防止传入的目录不可用
            image.save(f"{self.get_assets_path()}/output/{self.code}.png")
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
"""

if __name__ == "__main__":
    print(f"TEST CASE 1 START =======================\n")
    uuid = "test_1"
    code = VerifyCode(uuid).verify_code()
    print(f"为{uuid}生成的验证码为: {code}\n")
    print(f"TEST CASE 1 END =======================\n")

    print(f"TEST CASE 2 START =======================\n")
    uuid = "test_2"
    code = VerifyCode(
        uuid, config={"verify_code_save_path": f"{os.path.dirname(__file__)}/{uuid}/"}
    ).verify_code()
    print(f"为{uuid}生成的验证码为: {code}\n")
    print(f"TEST CASE 2 END =======================\n")
