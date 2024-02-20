class Movie:
    def __init__(self, title, prod_date, genre):
        self.title = title
        self.prod_date = prod_date
        self.genre = genre

        self._views = 0

    def __str__(self):
        return f"{self.title} ({self.prod_date})"
    
    def play(self, count=1):
        self._views += count
        return self._views
    
    def __contains__(self, item):
        return item in self.items
    


class Serial(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.episode = episode
        self.season = season
    
    def __str__(self):
        if self.season < 10:
            return f"{self.title} S0{self.season}E{self.episode}"
        elif self.episode < 10:
            return f"{self.title} S{self.season}E0{self.episode}"
        elif self.season < 10 and self.episode < 10:
            return f"{self.title} S0{self.season}E0{self.episode}"
        return f"{self.title} S{self.season}E{self.episode}"
        

movie_one = Movie(title="Pulp", prod_date=2012, genre="Action")
serial_one = Serial(title="The Simpsons", prod_date="1999", genre="Comedy", episode=10, season=4)

print(movie_one)
print(serial_one)