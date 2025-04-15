from sys import stdin

def pallindrome_check(s):

    if len(s) == 1:
        return True

    rev_str = ""
    for i in range(len(s)-1,-1, -1):
        rev_str = rev_str + s[i]
    
    if rev_str == s:
        return True
    else:
        return False

s = stdin.readline().strip()
if pallindrome_check(s):
    print('true')
else:
    print('false')