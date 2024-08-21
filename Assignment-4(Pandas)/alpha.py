# EngAlph, having 26 elements with the alphabets as values and default index values. 
import pandas as pd
alpha=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphaser=pd.Series(alpha)
print(alphaser)

#Find the dimensions, size and values of the Series EngAlph, Vowels, Friends, MTseries, MonthDays.
print("size=",alphaser.size)
print("Values=",alphaser.values)
print("Shape=",alphaser.shape)

#Display the alphabets ‘e’ to ‘p’ from the Series EngAlph.
sort=alphaser.iloc[4:16]
print(sort)

#Display the first 10 values in the Series EngAlph.
print(alphaser[:10])

#Display the last 10 values in the Series EngAlph.
print(alphaser[-10:])