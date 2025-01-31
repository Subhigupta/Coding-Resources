from sys import stdin

"""Constraints 
Do it in-place(no extra memory) and in single pass.
Changes should be made to the array itself.
"""

"""Method 1: Using two for loops. The time complexity
will be of order O(N2), so not feasible."""
def pushZerosAtEnd_1(arr, n) :
    for i in range(len(arr)):
        if arr[i]==0:
            for j in range(i+1, len(arr)):
                if arr[j]!=0:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    break #break the inner loop after searching
                          #condition has been satisfied.

"""Method 1: Doing in one single pass. Keeping a track of non zero indexes."""
def pushZerosAtEnd_2(arr, n):
    non_zero_idx = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            temp = arr[i]
            arr[i] = arr[non_zero_idx]
            arr[non_zero_idx] = temp
            non_zero_idx = non_zero_idx+1

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd_1(arr, n)
    printList(arr, n)

    t -= 1