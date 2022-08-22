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
    for page in range(1,50):
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
                    """ 
                    price.append(bit.find("span", {"class": "ad-price"}).get_text())
                    location.append(bit.find("div", {"class": "tile-location"}).get_text())
                    bedrooms.append(bit.find("div", {"class": "re-bedroom"}).get_text())
                    bathrooms.append(bit.find("div", {"class": "re-bathroom"}).get_text())
                    garage.append(bit.find("div", {"class": "car-parking"}).get_text())
                    area.append(bit.find("div", {"class": "surface-area"}).get_text())
                    """
                    price.insert(count,bit.find("span", {"class": "ad-price"}).get_text())
                    location.insert(count,bit.find("div", {"class": "tile-location"}).get_text())
                    bedrooms.insert(count,bit.find("div", {"class": "re-bedroom"}).get_text())
                    bathrooms.insert(count,bit.find("div", {"class": "re-bathroom"}).get_text())
                    garage.insert(count,bit.find("div", {"class": "car-parking"}).get_text())
                    area.insert(count,bit.find("div", {"class": "surface-area"}).get_text())
                    count += 1
                    print(count)
                except Exception:
                    pass
    return soup


#initialize function
get_rental_prices()

#assign stored data in lists to dataframe columns
df['location'] = pd.Series(location)
df['price'] = pd.Series(price)
df['bedrooms'] = pd.Series(bedrooms)
df['bathrooms'] = pd.Series(bathrooms)
df['garage'] = pd.Series(garage)
df['area'] = pd.Series(area)

#explore results
df.to_csv("rental_data.csv")
print(df)
