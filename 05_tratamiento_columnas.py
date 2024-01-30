import pandas as pd

ENCODING = 'ISO-8859-1'
df = pd.read_csv('datsets\car_crashes.csv', encoding = ENCODING)

print(df.head(1))

df = df.rename(columns = {'weekend' : 'fin_semana', 'Year' : 'anio'})

print(df.head(1))
