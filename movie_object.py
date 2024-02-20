# Klasa Film
class Movie:

    # Pobieranie danych
    def __init__(self, title, prod_date, genre):
        self.title = title
        self.prod_date = prod_date
        self.genre = genre

        self._views = 0
    # Wyswietlanie 
    def __repr__(self):
        return f"{self.title} ({self.prod_date})"
    # Ilosc ogladajacych
    def views(self):
        return self._views
    # Zwiekszanie ilosci ogladajacych
    def play(self):
        self._views += 1

# podklasa Serial
class Serial(Movie):
    # Pobieranie danych
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.episode = episode
        self.season = season
    # Wyswietlanie 
    def __repr__(self):
        if self.season < 10:
            return f"{self.title} S0{self.season}E{self.episode}"
        elif self.episode < 10:
            return f"{self.title} S{self.season}E0{self.episode}"
        elif self.season < 10 and self.episode < 10:
            return f"{self.title} S0{self.season}E0{self.episode}"
        return f"{self.title} S{self.season}E{self.episode}"
        

# klasa Biblioteka (przechowuje w liscie dane)
class Library:
    
    def __init__(self) -> None:
        self.library = []

    def store(self, instance):
        self.library.append(instance)

    def __repr__(self):
        for movie in self.library:
            print(movie.title, movie.prod_date)
        return ''

    def get_movies(self):
        return [movie for movie in self.library if type(movie) == Movie]
    
    def get_series(self):
        return [serial for serial in self.library if type(serial) == Serial]








# Instancje

Biblioteka = Library()



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

# Akcje Biblioteka
Biblioteka.store(movie_one)
Biblioteka.store(movie_two)
Biblioteka.store(movie_three)
Biblioteka.store(movie_four)
Biblioteka.store(movie_five)
Biblioteka.store(serial_one)
Biblioteka.store(serial_two)
Biblioteka.store(serial_three)
Biblioteka.store(serial_four)
Biblioteka.store(serial_five)

#print(Biblioteka)

print(Biblioteka.get_movies())
print(Biblioteka.get_series())



#print(movie_one)
#print(serial_one)
#movie_one.play()
#movie_one.play()
#print(movie_one.views())