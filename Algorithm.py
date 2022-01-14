# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 13:29:09 2021

@author: Johnny_Hang
"""


def binerySearch(lst, target):
    def binery(lst, target, left, right):
        while (left <= right):
            mid = (left+right)//2
            print(mid, left, right)
            if target == lst[mid]:
                return mid
            elif target < lst[mid]:
                right = mid-1
            else:
                left = mid+1
    n = len(lst)
    index = binery(lst, target, 0, n-1)
    return index


def BubbleSort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j+1] < lst[j]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
    return lst


def QuickSort(lst):
    def partition(lst, left, right):
        key = left
        while left < right:
            while lst[key] <= lst[right] and left < right:
                right -= 1
            while lst[key] >= lst[left] and left < right:
                left += 1
            lst[left], lst[right] = lst[right], lst[left]
        lst[key], lst[left] = lst[left], lst[key]
        return left

    def sort(lst, left, right):
        if left >= right:
            return lst
        mid = partition(lst, left, right)
        sort(lst, left, mid-1)
        sort(lst, mid+1, right)

        return lst

    sort(lst, 0, len(lst)-1)
    return lst


def InsertSort(lst):
    for i in range(0, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
    return lst


def ShellSort(lst):
    def InserSort(lst, n, x):
        for i in range(0, n, x):
            for j in range(i, 0, -x):
                if lst[j-1] > lst[j]:
                    temp = lst[j-1]
                    lst[j-1] = lst[j]
                    lst[j] = temp

    n = len(lst)
    p = n//2
    while p >= 1:
        InserSort(lst, n, p)
        print(lst)
        p = p//2
    return lst


def SelectSort(lst):
    for i in range(0, len(lst)):
        for j in range(i, len(lst)-1):
            temp = i
            if lst[i] > lst[j]:
                temp = j
        if i != temp:
            temp2 = lst[i]
            lst[i] = lst[temp]
            lst[temp] = temp2
    return lst


def HeapSort(lst):
    def Heap(lst, root, length):
        left = 2*root+1
        right = 2*root+2
        maxRode = root
        print(root, length)
        if left < length and lst[left] > lst[root]:
            maxRode = left
        if right < length and lst[right] > lst[maxRode]:
            print(maxRode)
            maxRode = right
        if maxRode != root:
            lst[maxRode], lst[root] = lst[root], lst[maxRode]
            Heap(lst, maxRode, length)
            return lst
        return lst
    n = len(lst)
    for i in range((n-1)//2, -1, -1):
        print(i)
        Heap(lst, i, n)
    while n > 0:
        print(n)
        lst[n-1], lst[0] = lst[0], lst[n-1]
        n -= 1
        Heap(lst, 0, n)

    return lst


def TwoWayMergeSort(lst):
    def Merge(lst, left, mid, right):
        arr = []
        i = left
        j = mid+1
        while i <= mid and j <= right:
            if lst[i] > lst[j]:
                arr.append(lst[j])
                j += 1
            else:
                arr.append(lst[i])
                i += 1
        while i <= mid:
            arr.append(lst[i])
            i += 1
        while j <= right:
            arr.append(lst[j])
            j += 1
        for k in range(left, right+1):
            lst[k] = arr[k-left]
        return lst

    def Sort(lst, left, right):
        if left >= right:
            return lst
        mid = (left+right)//2
        Sort(lst, left, mid)
        Sort(lst, mid+1, right)
        Merge(lst, left, mid, right)

        return lst

    Sort(lst, 0, len(lst)-1)
    return lst


def CountSort(lst):
    arr = []
    temp = [0]*(max(lst)+1)
    for i in lst:
        temp[i] += 1
    print(temp)
    for i in range(0, max(lst)+1):
        for j in range(0, temp[i]):
            arr.append(i)
    return arr


def BucketSort(lst):
    def SelectSort(lst):
        for i in range(0, len(lst)):
            temp = i
            for j in range(i, len(lst)):
                if lst[j] < lst[temp]:
                    temp = j
            if i != temp:
                lst[i], lst[temp] = lst[temp], lst[i]
        return lst
    arr = []
    buckets = []
    for i in range(0, max(lst)//10+1):
        buckets.append([])

    for j in lst:
        n = j//10
        buckets[n].append(j)
    for k in buckets:
        SelectSort(k)
        for j in k:
            arr.append(j)
    return arr


def RadixSort(lst):

    def Radix(item, num):
        item = item//(10**num)
        index = item % 10
        return index

    maxValue = max(lst)
    add = 1
    while maxValue > 9:
        maxValue = maxValue//10
        add += 1
    for k in range(0, add):
        Buckets = []
        arr = []
        for i in range(0, 10):
            Buckets.append([])
        for i in lst:
            index = Radix(i, k)
            Buckets[index].append(i)
        for i in Buckets:
            for j in i:
                arr.append(j)
        lst = arr
    return lst


def Fibonacci_iterative(num):
    if num <= 1:
        return 1
    lifib = 0
    hifib = 1
    for i in range(0, num):
        x = lifib
        lifib = hifib
        hifib = hifib+x
    return hifib


def Fib_recursion(num):
    if num <= 1:
        return 1
    return Fib_recursion(num-1)+Fib_recursion(num-2)


class STACK():
    def __str__(self):
        return "you r good"

    def __init__(self):
        self.stack = []

    def _IsEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Push(self, data):
        self.stack.append(data)

    def Pop(self):
        if self._IsEmpty():
            raise NotImplementedError('Initial＿data was not iterable data')
        else:
            return self.stack.pop()

    def Peek(self):
        if self._IsEmpty():
            raise NotImplementedError('Initial＿data was not iterable data')
        else:
            return self.stack[-1]


class Queue():
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def _IsEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def Push(self, data):
        self.queue.append(data)

    def Pop(self):
        if self._IsEmpty():
            raise NotImplementedError('the list is Empty')
        else:
            return self.queue.pop(0)


def con(a, b, **kwargs):
    print('{0} {2} {1}'.format(a, b, kwargs))

# con(c=1,a="Hello",b="myname")


def reverse(a):
    length = len(a)
    i = 0
    length = len(a)-1
    while i < len(a):
        if a[i] != a[length]:
            return False
        i += 1
        length -= 1
    return True


print(reverse('redder'))
print(reverse('alpha'))


def intersection(a, b):
    result = []
    for i in a:
        if (i in b) and (i not in result):
            result.append(i)
    result.sort()
    return result


print(intersection([1, 5, 9, 6, 5, 2], [5, 9, 8, 2, 10, 9]))
