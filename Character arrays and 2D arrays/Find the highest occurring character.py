from sys import stdin
import numpy as np

def highestOccuringChar(string) :
	#Your code goes here
	freq = {}
	for char in string:
		if char in freq.keys():
			freq[char] = freq[char] + 1
		else:
			freq[char] = 1

	max = np.max([value for value in freq.values()])
	max_char = ""
	for key in freq.keys():
		if freq[key] == max:
			max_char = key
			break
	
	return max_char
		
#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)