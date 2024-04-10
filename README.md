# MachineLearning
Repo with a bunch of ML projects that I am working with to get into the accelerating field of AI.

# Project 1:
## WebScraping movie tables on the net to compare movie budget and movie revenue
- Gathered data using a threaded script sending GET request to fetch a website's webpages (60 pages)
- Used BeautifulSoup to store to gather data per movie and store it onto a class
- Cleaned the data when passed into the Movie class's constructor
- Write to a tsv file 
- Create a Regression model (line of best fit) with 6492 clean data points in Google Collab