arr=[10,20,30,40,50]
max_value=max(arr)
min_value=min(arr)

def min_max_list(arr):
    for x in arr:
        result=(x-min_value)/(max_value-min_value)
        print("Result :", result)

min_max_list(arr)