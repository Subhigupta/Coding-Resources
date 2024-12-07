def staircase(n):
    #base case
    if n<0:
        return 0
    elif n==0:
        return 1
    
    a=staircase(n-1)#means I have climbed one step, rest is on recursion
    b=staircase(n-2)#means I have climbed two steps, rest is on recursion
    c=staircase(n-3)#means I have climbed three steps, rest is on recursion

    return a+b+c

n=int(input())
print(staircase(n))