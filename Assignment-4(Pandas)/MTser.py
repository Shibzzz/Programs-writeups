#MTseries, an empty Series. Check if it is an empty series.
import pandas as pd
MTseries=pd.Series()
empty=MTseries.empty
print(MTseries)
print("\nIs the series empty?",empty)

#Rename the Series MTseries as SeriesEmpty.
MTseries.name='SeriesEmpty'
print("Updated name = ",MTseries.name)

#Display the MTseries.
print(MTseries)