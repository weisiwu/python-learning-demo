""" 合并排序 - 归纳证明 """

def merge(left, right):
    newArr = []
    li, ri = 0, 0
    leftLen, rightLen = int(len(left)), int(len(right))
    while (li < leftLen and ri < rightLen):
        if (left[li] < right[ri]):
            newArr.append(left[li])
            li += 1
        else:
            newArr.append(right[ri])
            ri += 1
    newArr += list(left[li:])
    newArr += list(right[ri:])
    return newArr

def MergeSort(arr):
    left, right = [], []
    arrLen = len(arr)
    if(arrLen < 2):
        return arr
    else:
        mid = int(arrLen / 2)
        left = MergeSort(arr[:mid])
        right = MergeSort(arr[mid:])
    return merge(left, right)

array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(MergeSort(array))

""" 合并排序: 百度百科 """
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)

def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result
print(MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))