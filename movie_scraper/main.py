import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.imdb.com/list/ls055592025/")
epic_webpage = response.text

soup = BeautifulSoup(epic_webpage, "html.parser")

movie_list = soup.find_all(name="h3", class_="lister-item-header")

movie_titles = []
movie_rank = []
for movies in movie_list:
    title = movies.a.getText()
    movie_titles.append(title)
    rank = movies.find(name="span", class_="lister-item-index unbold text-primary").getText()
    movie_rank.append(rank)

num = 0
with open("movies.txt", mode="w") as file:
    for _ in movie_rank:
        contents = file.write(f"{movie_rank[num]} {movie_titles[num]}\n")
        num += 1