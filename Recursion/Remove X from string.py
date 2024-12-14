def remove(str,i):
    if i>=len(str):
        return str
    if str[i]=="x":
        return remove(str[0:i]+str[i+1:],i)
    else:
        i=i+1
        return remove(str,i)

str=input()
print(remove(str,i=0))