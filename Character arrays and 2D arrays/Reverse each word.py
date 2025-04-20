
from sys import stdin

#using split and join
def reverseEachWord_1(string) :
	# Your code goes here

    words = [word for word in string.split(" ")]
    rev_words  = []

    for word in words:
        rev_word = word[::-1]
        print(rev_word)
        rev_words.append(rev_word)
    
    string = ' '.join(rev_words)

    return string

def reverseEachWord_2(string) :
    s = list(string)
    print(s)
    ptrA = 0
    ptrB = 0
    i=0

    def swap(s, ptrA, ptrB):
        while ptrA < ptrB:
            s[ptrA], s[ptrB] = s[ptrB], s[ptrA]
            ptrA = ptrA+1
            ptrB = ptrB-1
        return s

    while i<len(s):
        if s[i] == ' ':
            ptrB = i-1
            s = swap(s, ptrA, ptrB)
            ptrA = i+1
            ptrB = ptrA

        elif i==len(s)-1:
            ptrB = i
            s = swap(s, ptrA, ptrB)
            ptrA = i+1
            ptrB = ptrA

        i = i+1
    return "".join(s)

#main
string = stdin.readline().strip()

ans = reverseEachWord_2(string)


print(ans)