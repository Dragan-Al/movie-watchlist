class Movie:
    def __init__(self, title, release_year, genre, imdb_url):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.imdb_url = imdb_url

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Year: {self.release_year}\n"
            f"Genre: {self.genre}\n"
            f"IMDb: {self.imdb_url}\n")