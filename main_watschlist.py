import pickle
import os
from movie import Movie

print("----------Welcome to Movie Watchlist app----------")

watchlist = []

if os.path.exists("watchlist.pkl"):
    with open("watchlist.pkl", "rb") as file:
        watchlist = pickle.load(file)
if(len(watchlist) > 0):
    print("\nAll books in the watchlist:")
    for movie in watchlist:
        print(movie)

while True:

    command = input("Command:\nAdd newMovie (1):\nShaw all movies (2):\nExit (3):\n")

    if command == "1":
        movie_title = input("Movie title: ") 
        movie_release_year = input("Movie release year: ") 
        movie_release_year = int(movie_release_year) 
        movie_genre = input("Movie genre: ")
        movie_imdb_url = input("Movie IMDB URL: ")

        movie = Movie(movie_title, movie_release_year, movie_genre, movie_imdb_url)
        watchlist.append(movie)
        with open("watchlist.pkl", "wb") as file:
            pickle.dump(watchlist, file)

        print(f"You have added a new movie: {movie_title}")

    elif command == "2":
        if len(watchlist) == 0:
            print("\nNo movies in the watchlist!\n")

        else:
            print("Movies in your watchlist:\n")
            for i in range(len(watchlist)):
                print(f"{i+1}. {watchlist[i]}\n")

    elif command == "3":
        break

    else:
        print("\nWrong command!\n")

print("\nHave a nice day.")
