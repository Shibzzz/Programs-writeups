import numpy as np

def calculate_variance(data):
    return np.var(data)

def calculate_deviation(data):
    return np.std (data)

def create_array(data):
    return np.array(data)

data = [10,20,30,40,50,60,70,80,90]

variance=calculate_variance(data)
deviation=calculate_deviation(data)
array=create_array(data)

print(f"array=",array)
print(f"variance=",variance)
print(f"deviation=",deviation)
