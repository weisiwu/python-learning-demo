import sys
import os
import webbrowser

# PIL: python imaging library，又称 pillow
# python中用于处理图片的库，用法参考
# https://zhuanlan.zhihu.com/p/58671158
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# desc: 该脚本执行后交互如下
# 1、输入要添加的文字
# 2、脚本扫码input文件夹下的所有符合要求的图片（png、webp、jpg）
# 3、将生成的图片放到 output 目录下
# 4、在终端提示任务完成和是否成功，成功并打开结果文件夹

# 读取输入的文字
text = input("请输入需要展示的数字\n")

# 更方便获取当前路径的方式: sys.path[0]
base_path = os.path.dirname(__file__)
input_path = f"{base_path}/input/"
files = os.listdir(input_path)


# https://www.programiz.com/python-programming/examples/file-name-from-file-path#google_vignette
# 从路径中获取文件名称
# print("无后缀", os.path.splitext(file_name)[0])
# print("有后缀", os.path.basename(file_name))


def handle_img(file_name, text):
    if file_name == "":
        raise ValueError("图片路径为空！")
    elif text == "":
        raise ValueError("文字为空！")
    else:
        # f 这种写法，是python中支持的字符串模板，通过f表示，字符串里嵌入了变量，变量用{}包裹
        full_file_name = f"{input_path}{file_name}"
        extension = sys.path[1]
        print("extension", extension)
        # 打开图片
        img = Image.open(full_file_name)
        w, h = img.size
        font_size = max(w * 0.05, 18)
        text_offset_left = int(len(text)) * font_size + font_size

        # 设置字体大小和位置
        font = ImageFont.truetype(f"{base_path}/font/msyh.ttc", font_size)
        print("尺寸:", w, h)
        # 开始重绘图片
        draw = ImageDraw.Draw(img)
        # 第一个参数，表示文字的落地位置。x、y坐标构成的元组
        draw.text((w - text_offset_left, 0), text, (255, 0, 0), font)
        img.save(f"{base_path}/output/{file_name}")


for file_name in files:
    handle_img(file_name, text)

# https://www.educative.io/answers/what-is-the-oslchflags-method-in-python
try:
    webbrowser.open(f"file://{base_path}/output/")
    print("处理完成")
except OSError as e:
    print("图片处理完成，但打开文件夹遇到错误: ", e)
