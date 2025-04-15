from sys import stdin

s = stdin.readline().strip()
i = 0
if len(s) !=1:
    while i<=len(s)-1:
        if s[i]==" ":
            s = s[:i] + s[i+1:]
        else:
            i = i+1

print(s)  