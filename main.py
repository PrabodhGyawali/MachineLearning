from bs4 import BeautifulSoup
import requests

URL = "https://www.the-numbers.com/movie/budgets/all"
response = requests.get(url=URL)
print(response.text)
    # Forbidden lmao
    

# soup = BeautifulSoup(, 'html.parser')

# print(soup.prettify())