import numpy as np

def sum(k):
    if k==0:
        return 1 #defining the base case
    else:
        return 1.0/(2**k) + sum(k-1) #recursively calculating the sum
    
k=int(input())
output=sum(k)

output="{:.5f}".format(output)

#Formatting basics:
# Syntax: str.format(value 1 , value2,...)
# {}: This indicates a placeholder for the value that will be formatted.
# .: Denotes the start of the formatting options.
# 5f: Specifies fixed-point notation with 5 digits after the decimal point.
# .format(output): Replaces the placeholder with the value of output, applying the specified formatting.

print(output)