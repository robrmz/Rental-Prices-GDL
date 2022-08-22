import pandas as pd

df = pd.read_csv("rental_data.csv")

##Strip price
df['price'] = df['price'].str.strip()
df['price'] = df['price'].str.strip("$")
df['price'] = df['price'].replace(',','', regex=True)

##Strip area so it doesn't show 'm2' legend
df['area'] = df['area'].str[:-3]

##Strip bedrooms, bathrooms and garage
df['bedrooms'] = df['bedrooms'].str.strip('+')
df['bathrooms'] = df['bathrooms'].str.strip('+')
df['garage'] = df['garage'].str.strip('+')



print(df)

df = df[['location', 'price', 'bedrooms', 'bathrooms','garage','area']]
df.to_csv("rental_data_formatted.csv")