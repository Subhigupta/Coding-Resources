def replace_str(s,i):
    if i==len(s):
        return s
    
    substr=s[i:i+2]
    #print(substr)
    if substr=="pi":
        #print(True)
        s=s[:i]+"3.14"+s[i+2:]
        #print(s)
        return replace_str(s,i+4)
    else:
        return replace_str(s,i+1)

s=input()
i=0
print(replace_str(s,i))