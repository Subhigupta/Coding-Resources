from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here

    elements = nRows*mCols
    rowLowLim =0
    rowUpLim = nRows-1

    colLowLim = 0
    colUpLim = mCols-1

    while elements>0:
        #print elements from left to right
        for i in range(colLowLim, colUpLim+1):
            print(mat[rowLowLim][i] , end=" ")
            elements = elements-1
        rowLowLim = rowLowLim+1

        if elements==0:
            break

        #print elements from top to bottom
        for i in range(rowLowLim, rowUpLim+1):
            print(mat[i][colUpLim], end=" ")
            elements = elements-1
        colUpLim = colUpLim -1

        #print elements from left to right
        for i in range(colUpLim, colLowLim-1, -1):
            print(mat[rowUpLim][i], end=" ")
            elements = elements-1
        rowUpLim =rowUpLim -1

        #print elements from bottom to up
        for i in range(rowUpLim, rowLowLim-1, -1):
            print(mat[i][colLowLim], end=" ")
            elements = elements-1
        colLowLim = colLowLim+1

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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1