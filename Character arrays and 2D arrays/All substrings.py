from sys import stdin

s = stdin.readline().strip()

for i in range(len(s)):
    print(s[i])
    for j in range(i+1, len(s), 1):
        sub_str = s[i:j+1]
        print(sub_str)
