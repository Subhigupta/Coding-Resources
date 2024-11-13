def count_zero(N,count):
    
    if (len(N)==1) & (N!='0'):
        return count
    elif (len(N)==1) & (N=='0'):
        count=count+1
        return count

    
    if (len(N)>=1) & (N[0]=='0'):
        count=count+1
        return count_zero(N[1:],count)
    else:
        return count_zero(N[1:],count)
    

N=int(input())
count=0
print(count_zero(str(N),count))