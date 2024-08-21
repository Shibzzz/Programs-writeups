#Friends, from a dictionary having roll numbers of five of your friends as data and their first name as keys.
import pandas as pd
friends=pd.Series([1,2,3,4,5],index=["Arun","Bibeesh","Dony","Fiza","Gunjan"])
print(friends)

#Name the index of the Series MonthDays as monthno and that of Series Friends as Fname.
friends.name='fname'
print("updated name=",friends.name)

#Display the 3rd and 2nd value of the Series Friends, in that order.
fr=friends.iloc[1:3]
print(fr)

