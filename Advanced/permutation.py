import numpy as np

def get_permutation(arr,i=0):
    if i==len(arr):
        return [arr.copy()]
    
    permutations = []
    for j in range(i,len(arr)):
        arr[i],arr[j]=arr[j],arr[i]
        permutations +=get_permutation(arr,i + 1)
        arr[i],arr[j]=arr[j],arr[i]

    return permutations

arr=np.array([1,2,3])
perms=get_permutation(arr.tolist())
print(np.array(perms))