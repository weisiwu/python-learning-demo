##-*-coding: utf-8-*-
import random

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
# 转化基数组为结果数组
for item in base_arr:
  # 转化
  for idx in range(0, 3):
  print(tmp)
  result.append(tmp)


# 生成9位的兑换码,由数字大小写构成
# @num {int} 指定生成的兑换码数目
# 生成算法描述:
# 1. 先准备一个包含[a-zA-Z0-9]的数组(不重复,62位)
# 2. 生成一个长200的结果数组,值的特征为: 001001001,即
# 分为3组,每组都为同样其序号值.
# 3. 对结果数组中的数值进行转化,将其每一位作为序号,换取
# 第一步准备的转换数组中对应的值.每转换3次,打乱一次转换
# 数组的顺序