from sys import stdin

"""Method 1"""
def rotate_1(arr, n, d):
    #Your code goes here
    sub_arr_1=arr[0:d]
    sub_arr_2=arr[d:n]

    for i in range(len(sub_arr_2)):
        arr[i]=sub_arr_2[i]
    for i in range(len(sub_arr_1)):
        arr[len(arr)-d+i]=sub_arr_1[i]

"""Method 2"""
def rotate_2(arr, n, d):
    #store first d elements
    first_d_ele=arr[0:d]

    #Shift all the elements from i+d pos to i pos
    for i in range(len(arr)-d):
        arr[i]=arr[i+d]
    
    #At last copy the d elements at the end of the array
    for i in range(len(first_d_ele)):
        arr[len(arr)-d+i]=first_d_ele[i]

"""Method 3"""
def rotate_3(arr,n,d):
    #Shift element at i+1 pos to ipos 
    while d>0:
        temp=arr[0]
        for i in range(len(arr)-d):
            arr[i]=arr[i+1]
        arr[i]=temp
        d-=1

"""Method 4"""
def rotate_4(arr,n,d):
    arr.reverse()
    sub_arr_1=arr[0:len(arr)-d]
    sub_arr_2=arr[len(arr)-d:n]

    for i in range(len(arr)-d):
        arr[i]=sub_arr_1[len(sub_arr_1)-1-i]
    print(arr)

    for i in range(d):
        arr[len(arr)-d+i]=sub_arr_2[len(sub_arr_2)-1-i]

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate_4(arr, n, d)
    printList(arr, n)
    
    t -= 1