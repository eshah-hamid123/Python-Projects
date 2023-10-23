from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
news_text = response.text
soup = BeautifulSoup(news_text, 'html.parser')
# all_anchor_tage = soup.find_all(name='a', class_= 'titlelink')
#
# for tag in all_anchor_tage:
#     print(tag.getText())

first_article = soup.find(name='a', class_='titlelink')
article_text = soup.find(name='a', class_='titlelink').getText()
# print(first_article.get('href'))

first_score = soup.find(name='span', class_='score')
# print(first_score.getText())

articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_urls = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    url = article.get('href')
    article_urls.append(url)

scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(article_texts)
# print(article_urls)
print(scores)

maxscore = max(scores)

index = scores.index(maxscore)
print(index)
print(article_texts[index])
print(article_urls[index])
# points = []
# for score in scores:
#     splitted_list = score.split()
#     point = int(splitted_list[0])
#     points.append(point)
#
# print(points)

