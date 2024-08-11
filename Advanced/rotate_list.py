def rotate_list(lst,k):
    if not lst:
        return lst
    k=k%len(lst)
    return lst[-k:]+lst[:-k]

my_list=[1,2,3,4]
k=int(input("Enter a number to rotate: "))
rotated_list=rotate_list(my_list,k)
print(rotated_list)