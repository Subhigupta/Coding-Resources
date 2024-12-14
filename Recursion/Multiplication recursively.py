def mult(N,M):
    if M==0:
        return 0
    if M>N:
        return mult(M,N) #this is done just for swapping purpose
                        #to avoid confusion always keeping N>M
    if N>=M:
        return N+ mult(N,M-1)

M=int(input())
N=int(input())
print(mult(N,M))