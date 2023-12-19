import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = (movie_titles[::-1])  # Reverse the list order

with open("Top 100 movies.txt", "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(f"{movie}\n")



