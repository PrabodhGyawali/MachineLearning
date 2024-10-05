import requests
import enum
from bs4 import BeautifulSoup
import threading
import json

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

# get_property_pages(filter)

def get_property_page_data():
    """
    Example of data structure:
        {
            'address': '2, Goff Street, Oxford, Oxfordshire OX2 8FW',
            'propertyType': 'Terraced',
            'bedrooms': 3,
            'images': {
                'imageUrl': '/spw/images/placeholder/no-image.svg',
                'mediumImageUrl': '/spw/images/placeholder/no-image.svg',
                'count': 0
            },
            'hasFloorPlan': False,
            'transactions': [
                {
                    'displayPrice': '£875,000',
                    'dateSold': '19 Jul 2024',
                    'tenure': 'Freehold',
                    'newBuild': False
                },
                {
                    'displayPrice': '£899,950',
                    'dateSold': '6 Oct 2021',
                    'tenure': 'Freehold',
                    'newBuild': True
                }
            ],
            'location': {
                'lat': 51.78529,
                'lng': -1.29468
            },
            'detailUrl': 'https://www.rightmove.co.uk/house-prices/details/england-21208984?s=6b9864a6de50d4376a93898838919d075a782568fb9704afc19c852657763fc4'
        }
    """
    with open('./html/page_1.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Server side rendering so info is stored in script tags
        scripts = soup.find_all('script')
        # Filter out script tags with no attributes
        scripts_no_attributes = [script for script in scripts if not script.attrs]
        
        # Get values inside script tags with housing info
        preloaded_data = scripts_no_attributes[2].contents[0]
        results = preloaded_data[29:]
        results_json = json.loads(results)
        print(results_json['results'])

def get_property_page_details(file_path):
    """
        Get the div 'root' id and extract features: gardent, EPC rating, parking, etc.
        Main features: number of bedrooms, bathrooms, property type, tenure, etc.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Server side rendering so info is stored in script tags
        scripts = soup.find_all('script')
        # Filter out script tags with no attributes
        scripts_no_attributes = [script for script in scripts if not script.attrs]
        
        # Get values inside script tags with housing info
        preloaded_data = scripts_no_attributes[2].contents[0]
        results = preloaded_data[29:]
        results_json = json.loads(results)
        print(results_json['results'])
