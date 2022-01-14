# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:37:01 2021

@author: Johnny_Huang
"""

def leetCode21(): #Merge Two Sorted Lists
    return None

def leetCode26(lst): #in-place algorithm
    if len(lst)==0:
        return 0
    i=0
    for j in range(1,len(lst)):
        if (lst[i]!=lst[j]):
            i+=1
            lst[i]=lst[j]
    return i+1    

def leetCode35(lst,tar):
    left=0
    right=len(lst)
    mid=0
    
    while left<=right:
        mid=(left+right)/2
        if lst[mid]==tar:
            return mid
        elif lst[mid]>tar:
            right=mid-1
        else:
            left=mid+1
    return left

import numpy as np
import matplotlib.pyplot as plt
import os
def aaaa():

    data=[-94.2,-98.2,-98,-98.2,-97.1,-96.4,-98.3,-98.5,-97.1,-98.1,-98.3,-98.2,-96.3,-96.2,-97.1,-97.3,-97.5,-96.2,-97.5,-94.8,-94.6,-95,-96.3,-97.3,-94.8,-93.9,-91.9,-92.1,-94.5,-95.9,-95.7,-96.2,-95.1,-95.3,-94.1,-92.6,-87.2,-89,-79.8,-87.6,-93.2,-95.8,-97.9,-96.1,-94.4,-89.3,-87.3,-87.2,-82.9,-82.3,-83.6,-88.1,-94.1,-97.3,-94.1,-94.6,-90.4,-81.2,-85.3,-83.2,-82.6,-79.8,-79.8,-86.8,-87.9,-89.7,-94.2,-86.5,-90.4,-86.2,-83.6,-81.4,-78.3,-74.3,-76.4,-78.8,-78.8,-73.4,-75.5,-77.6,-78.2,-80.5,-79.6,-74.8]
    a=len(data)
    # print(a)
    x=np.arange(a)/a-1
    # print(x)
    data.sort()
    # print(data)
    p=[1-i for i in x]
    print(p)
    
    
    d=[-74.3,-74.8,-75.5,-76.4,-77.6,-78.2,-78.3,-78.8,-78.8,-79.6,-79.8,-79.8,-79.8,-80.5,-81.2,-81.4,-82.3,-82.6,-82.9,-83.2,-83.6,-83.6,-85.3,-86.2,-86.5,-86.8,-87.2,-87.2,-87.3,-87.6,-87.9,-88.1,-89,-89.3,-89.7,-90.4,-90.4,-91.9,-92.1,-92.6,-93.2,-93.9,-94.1,-94.1,-94.1,-94.2,-94.2,-94.4,-94.5,-94.6,-94.6,-94.8,-94.8,-95,-95.1,-95.3,-95.7,-95.8,-95.9,-96.1,-96.2,-96.2,-96.2,-96.3,-96.3,-96.4,-97.1,-97.1,-97.1,-97.3,-97.3,-97.3,-97.5,-97.5,-97.9,-98,-98.1,-98.2,-98.2,-98.2,-98.3,-98.3]
    f=[0,0,0,0,0,0,0,0,0,0,0.022329099,0.033493649,0.044658199,0.044658199,0.063995766,0.075160316,0.094497883,0.105662433,0.125,0.144337567,0.163675135,0.174839684,0.194177252,0.205341801,0.216506351,0.227670901,0.25,0.272329099,0.294658199,0.316987298,0.328151848,0.347489415,0.369818514,0.392147614,0.403312164,0.422649731,0.43381428,0.453151848,0.472489415,0.491826982,0.514156082,0.533493649,0.552831216,0.572168784,0.591506351,0.591506351,0.602670901,0.625,0.644337567,0.655502117,0.674839684,0.686004234,0.705341801,0.716506351,0.735843918,0.755181486,0.774519053,0.796848152,0.81618572,0.838514819,0.849679369,0.860843918,0.880181486,0.891346035,0.902510585,0.902510585,0.902510585,0.902510585,0.913675135,0.924839684,0.936004234,0.955341801,0.966506351,0.977670901,1,1,1,1,1,1,1,1]
    plt.plot(d,f)
    plt.xlim(-100,-76)
    plt.ylim(0,1)
    plt.show()

def mkdirs_in_batch(path):
    try:
        path = os.path.normpath(path)
        path = path.replace('\\', '/')
        head, tail = os.path.split(path)
        print(head, tail)
        new_dir_path = ''
        isdir=False
        while isdir == False:
            if not os.path.isdir(head):
                head, tail = os.path.split(head)
                new_dir_path = new_dir_path+tail+ r"/"
                root = head
                print(head)
            else:
                isdir = True
        else:
            print(root,new_dir_path)
            # new_dir_path = root + new_dir_path
            new_dir_path = os.path.normpath(new_dir_path)
            print(new_dir_path)
            head, tail = os.path.split(new_dir_path)
            print(head, tail)
            temp = ''
            while tail:
                temp = temp + r"/"+ tail
                dir_path = root+temp
                print(dir_path,head,root)
                if not os.path.isdir(dir_path):
                    os.mkdir(dir_path)
                head, tail = os.path.split(head)

        return True
    except Exception as e:
        # logger.error('批量創建目錄出錯：{}'.format(e))
        return False
