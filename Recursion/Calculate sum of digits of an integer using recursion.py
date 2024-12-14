def sum(N):
    if N==0:
        return 0
    
    rem=N%10
    return rem + sum(int(N/10))

N=int(input())
print(sum(N))