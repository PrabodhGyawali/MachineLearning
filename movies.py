from datetime import datetime

class Movie:
    ReleaseDate: datetime
    Name: str
    Budget: int
    DomesticGross: int
    WorldWideGross: int
    def __init__(self, releaseDate, name, budget, domesticGross, worldWideGross):
        self.ReleaseDate = self.clean_date(releaseDate)
        self.Name = name
        self.Budget = self.clean_revenue(budget)
        self.DomesticGross = self.clean_revenue(domesticGross)
        self.WorldWideGross = self.clean_revenue(worldWideGross)
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
    
    def to_csv(self): # May be needed in the future
        pass
