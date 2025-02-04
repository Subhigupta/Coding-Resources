from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    i, pz, pt =0, 0, n-1
    while i<=pt:
        if arr[i] == 0:
            temp = arr[i]
            arr[i] = arr[pz]
            arr[pz] =temp

            pz = pz+1
            i = i+1
        elif arr[i] == 1:
            i =i+1
        else:
            temp = arr[i]
            arr[i] = arr[pt]
            arr[pt] =temp

            pt = pt-1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1