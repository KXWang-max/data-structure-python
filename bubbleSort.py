# -*- coding=utf-8 -*-
#冒泡排序，最优时间复杂度O(n),最坏O(n^2)，有稳定性
#两次循环，每次比较相邻两个元素的大小，进行排序

def bubble_sort(alist):
    #range(start,stop,step),[start,stop)取值为前闭后开区间，step默认为1，-1为倒着取，逐渐减小
    for j in range(len(alist)-1,0,-1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
