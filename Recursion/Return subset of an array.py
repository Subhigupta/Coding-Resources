def subsets(i,nums):
    if i>=len(nums):
        res.append(subset.copy())
        return
    
    subset.append(nums[i])
    subsets(i+1,nums)

    subset.pop()
    subsets(i+1,nums)

global res
global subset

res=[]
subset=[]

nums=[int(x) for x in input("Enter elements").split()]
subsets(0,nums)
print(res)