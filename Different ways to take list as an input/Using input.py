list=input("Enter a list")
print(type(list)) #Whatever you enter as input, input function converts it into a string.

list=[int(ele) for ele in input("Enter elements").split(",")] #If elements are passed as 1,2,3,4
print(list)

list=[int(ele) for ele in input("Enter elements").split(" ")] #If elements are passed as 1 2 3 4
print(list)