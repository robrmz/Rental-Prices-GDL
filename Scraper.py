#Here I will be building the scraper needed to 
#gather rental prices data for Zapopan/GDL

from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd 


#initialize categories as lists
price = []
location = []
bedrooms = []
bathrooms = []
garage = []
area = []

#initialize dataframe
df = pd.DataFrame()
#this will be the main 


def get_rental_prices():
    count = 0
    #iterate over each page on 'zapopan' results, adjust range as needed
    for page in range(1,3):
            url = 'https://www.vivanuncios.com.mx/s-renta-inmuebles/zapopan/v1c1098l14828p' + str(page)
            headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
            }

            #main requests/bs4 lines    
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            #iterate over each listing
            for bit in soup.find_all("div", {"class": "tileV2"}):
                #and iterate inside each listing
                try:
                    price.append(bit.find("span", {"class": "ad-price"}).get_text())
                    location.append(bit.find("div", {"class": "tile-location"}).get_text())
                    bedrooms.append(bit.find("div", {"class": "re-bedroom"}).get_text())
                    bathrooms.append(bit.find("div", {"class": "re-bedroom"}).get_text())
                    garage.append(bit.find("div", {"class": "re-bedroom"}).get_text())
                    area.append(bit.find("div", {"class": "re-bedroom"}).get_text())
                    count += 1
                    print(count)
                except Exception:
                    pass
    return soup


#initialize function
get_rental_prices()

#assign stored data in lists to dataframe columns
df['location'] = location
df['price'] = price
df['bedrooms'] = bedrooms
df['bathrooms'] = bathrooms
df['garage'] = garage
df['area'] = area

#explore results
print(df.columns)
