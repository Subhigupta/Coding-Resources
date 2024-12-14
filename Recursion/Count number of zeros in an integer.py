#Define the function to count zeros in an integer recursively
def count_zero(N,count):
    if (len(N)==1) & (N!='0'): #First base case, if only one integer is left and it's not zero
        return count
    elif (len(N)==1) & (N=='0'): #Second base case, if only one integer is left and it's zero
        count=count+1
        return count
    
    if (len(N)>=1) & (N[0]=='0'):
        count=count+1 #if integer is zero, increase the value of zero
        return count_zero(N[1:],count) #At each iteration, recursively sending integer 
                                        # with eliminating the starting integer 
    else:
        return count_zero(N[1:],count)#At each iteration, recursively sending integer 
                                    # with eliminating the starting integer 
    
N=int(input())
count=0
print(count_zero(str(N),count))