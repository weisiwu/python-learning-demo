##-*-coding: utf-8-*-
import random

def generate_code():
  trans_arr = result = []
  # 生成3个不同的转换数组
  for i in range(0, 3):
    tmp = list('abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789')
    random.shuffle(tmp)
    trans_arr.append(''.join(tmp))
  set(trans_arr)
  # 去重,并重新添加
  while len(trans_arr) < 3:
    tmp = list('abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789')
    random.shuffle(tmp)
    trans_arr.append(''.join(tmp))
    set(trans_arr)
  # 生成基数组: 001001001...
  base_arr = [ str(x).zfill(3)*3 for x in range(0, 200)]
  # 打开文件
  # 转化基数组为结果数组
  for item in base_arr:
    pa = pb = pc = ''
    # 转化
    for i in item[0:3]:
      pa += trans_arr[0][int(i)]
    for j in item[3:6]:
      pb += trans_arr[1][int(j)]
    for k in item[6:9]:
      pc += trans_arr[2][int(k)]
    # 将生成的激活码写入文件
    result.append(pa + pb + pc)
  return result