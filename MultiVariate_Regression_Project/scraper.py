import requests
from bs4 import BeautifulSoup

base_url = 'https://www.zoopla.co.uk/for-sale/property/oxford/'

params = {
    "Referer": "https://www.zoopla.co.uk/",
    "Sec-Ch-Ua-Platform": "Windows",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
response = requests.get(url=base_url, params=params)

if response.status_code == 200:
    # Scrape more info links for each property on the site
    print("success")
    pass
else:
    print(response.status_code)