from bs4 import BeautifulSoup, ResultSet, Tag
from movies import Movie
import os

movies = []
raw_data_paths = os.listdir("raw_data")

# Cleaner function that takes a list of table rows and extracts the movie data
def cleaner(table_rows: ResultSet[Tag]):
    movies_chunk = []
    for row in table_rows[1:]:
        fields = row.select("td") 
        # Create a movie object
        try:
            movie = Movie(
                fields[0].text ,fields[1].text, fields[2].text, fields[3].text, fields[4].text, fields[5].text
            )
            movies_chunk.append(movie)
        except Exception:
            continue
    movies.extend(movies_chunk)


# Loop through all the files in the raw_data folder
for raw_data_path in raw_data_paths:
    if raw_data_path.endswith(".html"):
        raw_data_0_path = f"raw_data/{raw_data_path}"
        # Reading the HTML file
        with open(raw_data_0_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Get the Header Table:
        table_rows = soup.select("tr")
        # Cleans data and appends to the movies list
        cleaner(table_rows)

for movie in movies:
    movie.to_csv("cleaned_data.csv")
            
print("Data cleaned and saved to 'cleaned_data.csv'")
print(len(movies))