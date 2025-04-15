
from sys import stdin


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
    ptrA = 0
    ptrB = 0
    i=0

    while True:
        if string[i] == ' ' or string[i] =='\0':
            ptrB = i-1

            while ptrA < ptrB:
                string[ptrA], string[ptrB] = string[ptrB], string[ptrA]
                
            ptrA = i+1
            ptrB = ptrA
            
            if string[i] == '\0':
                break

        i = i+1
    return string


#main
string = stdin.readline().strip()

ans = reverseEachWord_2(string)

print(ans)