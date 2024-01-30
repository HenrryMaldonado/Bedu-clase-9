import pandas as pd

ENCODING = 'ISO-8859-1'
df = pd.read_csv('datsets\car_crashes.csv', encoding = ENCODING)

print(df.size)
print(len(df))
print(df.iloc[1000])
