# MonthDays, from a numpy array having the number of days in the 12 months of a year. The labels should be the month numbers from 1 to 12.
import pandas as pd
monthdays=pd.Series([31,28,31,30,31,30,31,31,30,31,30,31],index=[1,2,3,4,5,6,7,8,9,10,11,12])
print(monthdays)

#Name the index of the Series MonthDays as monthno and that of Series Friends as Fname.
monthdays.name='monthno'
print('updated name = ', monthdays.name)

