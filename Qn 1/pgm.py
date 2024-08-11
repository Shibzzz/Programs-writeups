data = [10,20,30,40,50,60,70,80,90]

def calculate_mean (data):
    return sum(data)/len(data)

def calculate_variance(data):
    mean=calculate_mean(data)
    sqrdf=[(x-mean)**2 for x in data]
    variance = sum(sqrdf)/len(data)
    return variance

def calculate_deviation(data):
    variance=calculate_variance(data)
    dev=variance ** 0.5
    return dev


def create_array(data):
    return list(data)

array=create_array(data)
mean=calculate_mean(data)
variance=calculate_variance(data)
deviation=calculate_deviation(data)


print(f"array=", data)
print(f"mean=", mean)
print(f"variance=", variance)
print(f"deviation", deviation)


    