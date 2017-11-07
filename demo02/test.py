y = list('abcdefg')
x = '000000'
for j in range(0,2):
  for i in x:
    print(y[int(i):int(i)+1])