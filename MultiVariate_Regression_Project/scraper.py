import requests
import enum
from bs4 import BeautifulSoup
import threading

PropertyType = enum.Enum(
    'DETACHED',
    'SEMI_DETACHED',
    'TERRACED',
    'FLAT',
    'LAND',
    'OTHER'
)
          

class Filter:
    def __init__(self, page, tenure='any', radius=0):
        self.radius = radius
        self.tenure = tenure
        self.page = page
        
    
    def generate_url(self):
        url = f'https://rightmove.co.uk/house-prices/oxford.html?'
        if self.radius != 0:
            return url + f'radius={self.radius}&'
        if self.tenure != 'any':
            return url + f'tenure={self.tenure}&'
        
        return url
        
    
class Property:
    def __init__(self, price, bedrooms, bathrooms, address, postcode, distance):
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.address = address
        self.postcode = postcode
        self.distance = distance

def get_property_pages(filter: Filter):
    url = filter.generate_url()
    for page in range(1, filter.page):
        response = requests.get(url + f'page={page}')
        if response.status_code == 200:
            with open(f'./html/page_{page}.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
        else:
            print(f"Failed to retrieve page {page}")

def calculate_distance_from(long, lat):
    pass

filter = Filter(50)

get_property_pages(filter)
