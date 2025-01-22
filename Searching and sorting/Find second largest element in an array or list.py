import numpy as np
from sys import stdin

def takeInput():
    n=int(stdin.readline().rstrip())

    if n!=0:
        arr=[int(ele) for ele in stdin.readline().rstrip().split(" ")]
        return arr, n
    
    return list(), n
    
"""Method 1 : Find firat max element, remove it and then find second largest."""
def secondLargestElement_1(arr, n):
    #write your code here
    first_max=np.max(arr)

    arr.remove(first_max)

    second_max=np.max(arr)
    
    return second_max

"""Method 2 : Sort an array and then find the second largest element."""
def secondLargestElement_2(arr, n):
    arr.sort(reverse=True)

    second_max=arr[1]

    return second_max

"""Method 3 : Scan the array once and keep updating first and second largest."""
def secondLargestElement_3(arr, n):

    first_max=0
    second_max=0

    for ele in arr:
        if ele > first_max:
            temp = first_max
            first_max = ele
            second_max = temp
        elif ele < first_max:
            if ele > second_max:
                second_max = ele

    return second_max



arr, n = takeInput()
print(secondLargestElement_3(arr, n))