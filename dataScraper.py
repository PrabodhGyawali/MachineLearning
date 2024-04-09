import requests
import json
import threading
import timeit

URL = "https://www.the-numbers.com/movie/budgets/all"

with open("request-data\\browserHeader.json", "r") as file:
    header_string = file.read()

header = json.loads(header_string)

# Write file contents into a document
def write_raw_data(http_response_text, file_name):
    root_path = "raw_data/"
    with open(root_path + file_name, "w", encoding="utf-8") as file:
        file.write(http_response_text)

response = requests.get(url=URL, headers=header)

# store response.text into a file
write_raw_data(response.text, "Raw-Data-0.html")

# Thread this task to make it really fast as we have to scrape 100+ pages
def scraper():
    URL_MORE = URL + f"/{i}01"
    response = requests.get(url=URL_MORE, headers=header)

    file_name = f"Raw-Data-{i}.html"
    write_raw_data(response.text, file_name)

for i in range(1, 65):
    thread = threading.Thread(target=scraper)
    thread.start()

# Measuring time it takes for the code to execute
timeit.timeit(scraper)




