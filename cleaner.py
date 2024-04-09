from bs4 import BeautifulSoup, ResultSet, Tag
from movies import Movie

raw_data_0_path = "raw_data/Raw-Data-0.html"
with open(raw_data_0_path, "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Get the Header Table:
table_rows = soup.select("tr")

# Variable to store movie objects of all the files
movies = []
def cleaner(table_rows: ResultSet[Tag]):
    movies_chunk = []
    for i in range(1, 101):
        row = table_rows[i]
        fields = row.select("td") 
        # Create a movie object
        movie = Movie(fields[1].text, fields[2].text, fields[3].text, fields[4].text, fields[5].text)
        movies_chunk.append(movie)
    movies.extend(movies_chunk)

cleaner(table_rows)

print(movies)