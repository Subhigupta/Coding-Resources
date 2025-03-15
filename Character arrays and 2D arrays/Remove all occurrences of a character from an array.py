
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	j = 0
	i = 0
	while i < len(string):
		if string[i] == ch:
			i = i+1
		elif string[i] != ch:
			string = string[:j] + string[i] + string[j+1:]
			i = i+1
			j = j+1

	string = string[:j] 

	return string

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)