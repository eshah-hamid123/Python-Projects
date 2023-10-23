import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_text = response.text
soup = BeautifulSoup(movie_text, 'html.parser')

movie_list = soup.find_all(name='h3', class_='title')

movie_names = [movie.getText() for movie in movie_list]
movie_names.reverse()
# print(movie_names)

with open ('movies.txt', 'w',  encoding="utf8")as file:
    for movie in movie_names:
        file.write(f'{movie}\n')
