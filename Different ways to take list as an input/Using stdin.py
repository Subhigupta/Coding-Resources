"""Stdin stands for standard input which is a stream from which the program reads its input data.
This method is slightly different from the input() method as it also reads the escape character 
entered by the user.
"""

import sys 
  
name = sys.stdin.readline() #a new line is getting printed
print(name) 

name=sys.stdin.readline().rstrip() #no new line is getting printed.
                                   #The rstrip() method removes any trailing characters 
                                   # (characters at the end a string)
print(name)

# num = sys.stdin.readline(2) # this method also provides the parameter for the size 
#                             # i.e. how many characters it can read at a time.
# print(num)

list=[int(ele) for ele in sys.stdin.readline().rstrip().split(" ")]
print(list)

print(sys.stdin.readline().rstrip().split(" "))