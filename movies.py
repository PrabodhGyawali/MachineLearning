from datetime import datetime

class Movie:
    Id: int
    ReleaseDate: datetime
    Name: str
    Budget: int
    DomesticGross: int
    WorldWideGross: int
    def __init__(self, id, releaseDate, name, budget, domesticGross, worldWideGross):
        self.Id = int(id)
        self.ReleaseDate = self.clean_date(releaseDate)
        self.Name = self.clean_name(name)
        self.Budget = self.clean_revenue(budget)
        self.DomesticGross = self.clean_revenue(domesticGross)
        self.WorldWideGross = self.clean_revenue(worldWideGross)
    
    def clean_name(self, text) -> str:
        # Cleans the name of the movie to remove ',' and '\n' characters
        return text.strip().replace(',', '').replace('\n', '')
    
    def clean_date(self, date) -> datetime:
        # Cleans the format: 'Dec 9, 2022' --> Datetime object
        date_object = datetime.strptime(date, '%b %d, %Y')
        return date_object

    def clean_revenue(self, revenue) -> int:
        # Cleans the format: '\xa0$2,317,514,386' --> 2317514386

        # Split string by '$'
        revenue = revenue.split('$')[1]
        # Remove commas
        revenue = revenue.replace(',', '')
        # Convert to integer
        revenue = int(revenue)
        return revenue
    
    def to_csv(self, file_path): # May be needed in the future
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{self.Id},{self.Name},{self.ReleaseDate.isoformat()},{self.Budget},{self.DomesticGross},{self.WorldWideGross}\n"
                )
