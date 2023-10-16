import os
from tabulate import tabulate

iphone_height=1136
iphone_width=640

def resize_img(img_obj):
    pass

"""
英语单词均以空格进行分割（无视语义）按照空格，分割出所有单词。
"""
if __name__ == "__main__":
    file_name = "The Impact of Technology on Society.txt"

    with open(os.path.join(os.path.dirname(__file__), f"./{file_name}"), "r") as file:
        words_info = resize_img(file)
