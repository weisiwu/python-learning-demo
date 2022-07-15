##-*-coding: utf-8-*-
import random

# 思路描述:
# 生成9位的兑换码,由数字大小写构成
# @num {int} 指定生成的兑换码数目
# 生成算法描述:
# 1. 先准备一个包含[a-zA-Z0-9]的数组(不重复,62位)
# 2. 生成一个长200的结果数组,值的特征为: 001001001,即
# 分为3组,每组都为同样其序号值.
# 3. 对结果数组中的数值进行转化,将其每一位作为序号,换取
# 第一步准备的转换数组中对应的值.每转换3次,打乱一次转换
# 数组的顺序

trans_arr = result = []
# 生成3个不同的转换数组
for i in range(0, 3):
  tmp = list('abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789')
  random.shuffle(tmp)
  trans_arr.append(''.join(tmp))
# 生成基数组: 001001001...
base_arr = [ str(x).zfill(3)*3 for x in range(0, 200) ]
# 打开文件
output = open('activeCode.txt', 'w')
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
  output.write(pa + pb + pc + '\n')

print('200个随机码生成完毕!')