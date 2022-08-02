# 图 广度优先(BFS) 寻找最短路径 树是有方无环图
# 下面的BFS并并非针对二叉树
from collections import deque

"""
图(非二叉树)的bfs
python 常见队列: https://blog.csdn.net/weixin_43533825/article/details/89155648
python deque:
    https://blog.csdn.net/weixin_43790276/article/details/107749745
    https://www.cnblogs.com/djdjdj123/p/15412639.html
"""

# 创建出来图，图关系依据images/graph.png绘制
graph = {
    "Me": ["Beli", "Clark", "David"],
    "Bob": ["Clark", "Ken"],
    "David": ["Bob", "Ken"],
    "Clark": [],
    "Ken": [],
    "Beli": [],
    "Frankly": ["Me", "Beli"]
}

def search4Name(name):
    # 将关联人全部放入搜索队列
    searchQueue = deque()
    searchQueue += graph['Me']
    searched = []
    while searchQueue:
        person = searchQueue.popleft()
        if person not in searched:
            if person == name:
                return True
            else:
                searchQueue += graph[person]
                searched.append(person)

    return False

# Q1: me->bob 是否有连线
path4bob = search4Name('Bob')
print('Bob: '+str(path4bob))

# Q2: me->ken 是否有连线
path4ken = search4Name('Ken')
print('Ken: '+str(path4ken))

# Q3: me->frankly 是否有连线
path4frankly = search4Name('Frankly')
print('Frankly: '+str(path4frankly))