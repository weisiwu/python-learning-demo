import os
from PIL import Image

ios5_size=(640, 1136)
img_folders=os.path.join(os.path.dirname(__file__), "imgs")
output_folders=os.path.join(os.path.dirname(__file__), "output")

def is_image_file(file_path):
    try:
        with Image.open(file_path) as img:
            # 能打开，则是图片
            return True
    except Exception as e:
        # 打开失败，文件非图片
        return False

def trans_by_ratio(img_path, img):
    img_obj=Image.open(img_path)
    (width, height)=img_obj.size
    # 计算等比例缩放后的图片尺寸
    w_ratio=width/ios5_size[0]
    h_ratio=height/ios5_size[1]
    final_ratio=1
    if w_ratio >= h_ratio:
        final_ratio=w_ratio
    else:
        final_ratio=h_ratio
    
    new_width=int(width/final_ratio)
    new_height=int(height/final_ratio)
    # 注意，这里resize后，要重新保持图片对象
    img_obj=img_obj.resize((new_width, new_height))
    
    # 画出iphone5分辨率大小的画布
    background=Image.new('RGB', ios5_size, (255, 255, 255))
    
    # 计算图片在背景的位置
    x=(ios5_size[0] - new_width) // 2
    y=(ios5_size[1] - new_height) // 2
        
    output_path=os.path.join(output_folders, f'resize_ratio_{img}')
    background.paste(img_obj, (x,y))
    background.save(output_path)

    img_obj.close()
    background.close()
    print(f'等比例缩放 ============> {img}转换成功')

def trans_by_size(img_path, img):
    output_path=os.path.join(output_folders, f'resize_{img}')
    img_obj=Image.open(img_path)
    img_obj.resize(ios5_size).save(output_path)
    img_obj.close()
    print(f'按尺寸缩放 ============> {img}转换成功')

"""
英语单词均以空格进行分割（无视语义）按照空格，分割出所有单词。
"""
if __name__ == "__main__":

    print('============ 不按照比例转换 ============')
    
    for img in os.listdir(img_folders):
        img_path=os.path.join(img_folders, img)
        if is_image_file(img_path):
            trans_by_size(img_path, img)
        
    print('============ 按照比例转换 ============')

    for img in os.listdir(img_folders):
        img_path=os.path.join(img_folders, img)
        if is_image_file(img_path):
            trans_by_ratio(img_path,img)