from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here

    if n==0 and m==0:
        output = 0

    elif n>0 and m==0:
        idx1, idx3, carry = len(arr1)-1,  len(output)-1, 0
        idx2 = 0

        while idx1>=0:
            output[idx3] = arr1[idx1] 

            idx1 =idx1 -1
            idx3= idx3-1

    elif n==0 and m>0:
        idx2, idx3, carry =  len(arr2)-1, len(output)-1, 0
        idx1 = 0

        while idx2>=0:
            output[idx3] = arr2[idx2]

            idx2 = idx2-1
            idx3= idx3-1

    else:
        idx1, idx2, idx3, carry = len(arr1)-1, len(arr2)-1, len(output)-1, 0

        while idx1>=0 and idx2>=0:
            sum_ele = arr1[idx1] + arr2[idx2] +carry 
            output[idx3] = int(sum_ele%10)
            carry = int(sum_ele/10)

            idx1=idx1-1
            idx2 = idx2-1
            idx3= idx3 -1

        #print(output)

        while idx2>=0:
            sum_ele = arr2[idx2] + carry
            output[idx3] = int(sum_ele%10)
            carry = int(sum_ele/10)

            idx2 = idx2-1
            idx3= idx3 -1


        while idx1>=0:
            sum_ele = arr1[idx1] + carry
            output[idx3] = int(sum_ele%10)
            carry = int(sum_ele/10)

            idx1=idx1-1
            idx3= idx3 -1

        output[idx3] =carry

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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1