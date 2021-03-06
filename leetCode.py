# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:37:01 2021

@author: Johnny_Huang
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Merge Two Sorted Lists
def leetCode21():
    temp = ListNode(None)
    prev = temp

    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    if l1:
        prev.next = l1
    if l2:
        prev.next = l2

    return prev.next


def leeteCode94():  # -> List[int]:
    arr = []
    stack = []
    # def traverse(root):
    #     if root==None:
    #         return
    #     traverse(root.left)
    #     arr.append(root.val)
    #     traverse(root.right)
    # traverse(root)

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        arr.append(root.val)
        root = root.right

    return arr


def leeteCode24():
    dummy = ListNode(None)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        temp1 = current.next  # ->head
        temp2 = current.next.next
        temp1.next = temp2.next
        temp2.next = temp1
        current.next = temp2
        current = current.next.next

    return dummy.next


def leeteCode997(n, trust):
    person = []
    for i in range(n):
        person.append([0, 0])  # trust trusted

    for i in trust:
        person[i[0]-1][0] += 1
        person[i[1]-1][1] += 1

    for i in range(0, n):
        if person[i][0] == 0 and person[i][1] == n-1:
            return i+1
    return -1


def leetCode26(lst):  # in-place algorithm
    if len(lst) == 0:
        return 0
    i = 0
    for j in range(1, len(lst)):
        if (lst[i] != lst[j]):
            i += 1
            lst[i] = lst[j]
    return i+1


def leetCode35(lst, tar):
    left = 0
    right = len(lst)
    mid = 0

    while left <= right:
        mid = (left+right)/2
        if lst[mid] == tar:
            return mid
        elif lst[mid] > tar:
            right = mid-1
        else:
            left = mid+1
    return left


def leeteCode167(arr, target):
    left = 0
    right = len(arr)-1

    while (arr[left]+arr[right] != target):
        while arr[left]+arr[right] > target and left < right:
            right -= 1
        while arr[left]+arr[right] < target and left < right:
            left += 1

    return [left+1, right+1]


def leeteCode26(arr):
    k = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[k]:
            k += 1
            arr[k] = arr[i]
            if k != i:
                arr[i] = '_'
        else:
            arr[i] = "_"
        print(arr, k, i)

    # [1, 2, 2, 2, 2, 2, 2, 4, 6, 7, 8, 9, 9, 9, 9] ->[1, 2, 4, 6, 7, 8, 9, '_', '_', '_', '_', '_', '_', '_', '_']
    return k+1


if __name__ == '__main__':
    # a = leeteCode26([1, 2, 2, 2, 2, 2, 2, 4, 6, 7, 8, 9, 9, 9, 9])
    # a = leeteCode26([1, 2, 2, 2, 4, 6, 7, 8, 9, 9, 9, 9])
    a = leeteCode997(2, [[1, 2]])
    print(a)
