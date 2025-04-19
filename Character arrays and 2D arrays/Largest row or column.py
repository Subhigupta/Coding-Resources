'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    sum_rows  = 0
    sum_cols = 0

    max_rows = 0
    idx_rows = 0

    idx_cols = 0

    rowTrue = True

    for i in range(nRows):
        sum_rows = 0
        for j in range(mCols):
            sum_rows = sum_rows + arr[i][j]
        if sum_rows > max_rows:
            max_rows = sum_rows
            idx_rows = i
    
    max_cols = max_rows
    for i in range(mCols):
        sum_cols = 0
        for j in range(nRows):
            sum_cols = sum_cols + arr[j][i]
        if sum_cols > max_cols:
            max_cols = sum_cols
            idx_cols = i
            rowTrue = False

    if max_rows==0 & max_cols==0:
        print("row 0 -2147483648")
    
    else:
        if rowTrue == False:
            print("column" + " " + str(idx_cols)+ " "+ str(max_cols))
        else:
            print("row" + " " + str(idx_rows)+ " "+ str(max_rows))
    


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1