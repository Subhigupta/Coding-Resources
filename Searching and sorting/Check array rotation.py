
from sys import stdin
import copy

def arrayRotateCheck_1(arr, n):
    #Your code goes here
    if n==0:
        return 0
    
    k = 0
    sort_arr = arr.copy()
    sort_arr.sort()
    ele_search = sort_arr[0]

    for i in range(len(arr)):
        if arr[i] == ele_search:
            k = i
            return k

def arrayRotateCheck_2(arr, n):
    if n==0:
        return 0
    
    k=0
    idx = 0
    for i in range (len(arr)):
        if arr[idx] > arr[i]:
            k = i-idx
            return k

def arrayRotateCheck_3(arr, n):
    if n==0:
        return 0
    
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            return i+1
            

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck_3(arr, n))

    t -= 1