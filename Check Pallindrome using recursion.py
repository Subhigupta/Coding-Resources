#Define a function to reverse a string recursively
def reverse_string(s):
    if len(s)==1: # defining the base case
        return s
    else:
        return s[len(s)-1]+reverse_string(s[:len(s)-1]) #at each iteration adding the character 
                                                        #present at last index of the string

#Define the function to check whether string is pallindrome or not 
def check_pallindrome(s):
    reverse_str=reverse_string(s)
    if s==reverse_str:
        return True
    else:
        return False

s=input("Enter a string")
print(check_pallindrome(s))