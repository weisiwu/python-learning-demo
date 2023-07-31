#-*-coding: utf-8-*-
import sys
# PIL: python imaging library,主要是在python2中使用.在python3中改为pillow库
# https://zhuanlan.zhihu.com/p/58671158
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# desc: 该脚本执行如下
# 1、输入你要写的数字
# 2、输入你要修改的图片: 只能在 demo1.jpg demo2.jpg demo3.jpg
# 3、获取脚本同目录下的demo.jpg,并做调整生成result.jpg
# 4、打开生成的图片

# 读取输入的数字
num = input('输入你要显示的数字: ')
imgName = input('输入对哪个图片进行操作: ')
# 计算一行展示的文字宽度，防止超出图片可视区域，被遮盖
# 偏移值因为汉字(全角)和数字、字母(半角)宽度有差异，所以不同。
strlen = int(len(num)) * 18

# 获取当前路径
imgPath = sys.path[0]

# 在内存中打开图像
targetImg = Image.open(imgPath + '/' + imgName)
# 设置字体和大小
font = ImageFont.truetype(imgPath + '/font/msyh.ttc', 18)
# 获取图片大小
w, h = targetImg.size
# 开始添加文字
draw = ImageDraw.Draw(targetImg)
draw.text((w - strlen, 0), num, (255, 0, 0), font)
draw = ImageDraw.Draw(targetImg)
# 保存新图片
targetImg.save(imgPath + "/result_" + imgName)

# 展示结果图片
targetImg.show()
print("修改图片成功")