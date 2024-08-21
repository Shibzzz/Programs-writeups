
data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

values = list(data.values())

mean = sum(values) / len(values)

sorted_values = sorted(values)
n = len(sorted_values)

if n % 2 == 0:
    median = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
else:
    median = sorted_values[n // 2]

mean_diff_squared_sum = sum((x - mean) ** 2 for x in values)
standard_deviation = (mean_diff_squared_sum / (n - 1)) ** 0.5

print("Mean =", mean)
print("Median =", median)
print("Standard Deviation =", standard_deviation)
