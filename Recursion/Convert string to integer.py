
def conversion(string,i):

    if i==len(string):
        return string
    
    if i==0 and string[i]=='0' and len(string)>1:
        return conversion(string[i+1:],i)
    
    nos=[f"{i}" for i in range(0,10)]
    #print(nos)
    if string[i] in nos: #we can also use string[i].isnumeric() 
        return conversion(string,i+1)
    else:
        return conversion(string[i+1:],i)
    
s=input()
i=0
print(conversion(s,i))