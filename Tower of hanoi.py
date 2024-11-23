def towerofhanoi(n, source, aux, dest):
    if n==0:
        return
    
    #First put all n-1 disks from source to auxillary
    #Finally place the largest disk on the destination rod
    #Then put all n-1 rods from auxillary to destination
    towerofhanoi(n-1,source,dest,aux) #auxillary is the destination for first moving n-1 disks
    print(source,dest)
    towerofhanoi(n-1,aux,source,dest) #then finally move those n-1 disks from auxillary to destination

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
