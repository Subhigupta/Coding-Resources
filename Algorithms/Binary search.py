def binary_search(array,target):
    l=0
    r=len(array)-1
    while l<=r:
        m=(l+r)//2
        if array[m]>target:
            r=m-1
        elif array[m]<target:
            l=m+1
        else:
            return m
    return -1

array=[int(x) for x in input("Enter elements").split()] # Forming a list of integers
target=int(input("Enter a element to search")) # Specifying integer to be searched
print(binary_search(array,target))
