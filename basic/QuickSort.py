""" 快排 - 归纳证明 """
def QuickSort(arr):
    arrLen = int(len(arr))
    if (arrLen < 2):
        return arr
    else:
        poviot = arr.pop()
        left, right = [], []
        for item in arr:
            if (item < poviot):
                left.append(item)
            else:
                right.append(item)
    return QuickSort(left) + [poviot] + QuickSort(right)

testArr = [1,2,36,7,30,90,68,51,4]
print(QuickSort(testArr))


"""快速排序: 百度百科"""    
def quick_sort(data):    
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return data
 
# 示例：
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quick_sort(array))
# 输出为[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]