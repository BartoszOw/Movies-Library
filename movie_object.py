class Movie:
    def __init__(self, title, prod_date, genre):
        self.title = title
        self.prod_date = prod_date
        self.genre = genre

        self._views = 0

    def __str__(self):
        return f"{self.title} ({self.prod_date})"
    
    def views(self):
        return self._views
    
    def play(self):
        self._views += 1


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
movie_two = Movie(title="Meg", prod_date=2000, genre="Horror")
movie_three = Movie(title="Kevin", prod_date=1999, genre="Comedy")
movie_four = Movie(title="Beekeeper", prod_date=2024, genre="Action")
movie_five = Movie(title="Marvel", prod_date=2020, genre="Sci-fi")

serial_one = Serial(title="The Simpsons", prod_date="1999", genre="Comedy", episode=10, season=4)
serial_two = Serial(title="Breaking Bad", prod_date="2005", genre="Action", episode=20, season=5)
serial_three = Serial(title="The Walking Dead", prod_date="2010", genre="Horror", episode=25, season=13)
serial_four = Serial(title="Lucifer", prod_date="1999", genre="Sci-fi", episode=15, season=3)
serial_five = Serial(title="Bears", prod_date="1999", genre="Documental", episode=5, season=1)


print(movie_one)
print(serial_one)
movie_one.play()
movie_one.play()
print(movie_one.views())