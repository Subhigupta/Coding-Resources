from sys import stdin

## Read input as specified in the question.
## Print output as specified in the question.
def replace_char(s,ch1,ch2):
    if len(s)==1:
        return s
    
    for i in range(len(s)):
        if s[i]==ch1:
            s = s[:i] + ch2 + s[i+1:]
    
    return s
    
s = stdin.readline().strip()
char = stdin.readline().strip()
print(char[0], char[2])
c1 = char[0]
c2 = char[2]
print(replace_char(s,c1,c2))