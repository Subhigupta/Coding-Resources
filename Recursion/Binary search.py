def binary_search(array,target,l,r):
    if l<=r:
        m=(l+r)//2
        if array[m]>target:
            return binary_search(array,target,l,m-1)
        elif array[m]<target:
            return binary_search(array,target,m+1,r)
        else:
            return m
    else:
        return -1


array=[int(x) for x in input("Enter elements").split()] # Forming a list of integers
target=int(input("Enter a element to search")) # Specifying integer to be searched
l=0
r=len(array)-1
print(binary_search(array,target,l,r))
