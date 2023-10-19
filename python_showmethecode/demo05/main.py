import os
from PIL import Image

def is_image_file(file_path):
    try:
        with Image.open(file_path) as img:
            # 能打开，则是图片
            return True
    except Exception as e:
        # 打开失败，文件非图片
        return False

"""
英语单词均以空格进行分割（无视语义）按照空格，分割出所有单词。
"""
if __name__ == "__main__":
    ios5_size=(640, 1136)
    img_folders=os.path.join(os.path.dirname(__file__), "imgs")
    output_folders=os.path.join(os.path.dirname(__file__), "output")
    
    for img in os.listdir(img_folders):
        img_path=os.path.join(img_folders, img)
        if is_image_file(img_path):
            output_path=os.path.join(output_folders, f'resize_{img}')
            img_obj=Image.open(img_path)
            img_obj.resize(ios5_size).save(output_path)
            print(f'============> {img}转换成功')
        