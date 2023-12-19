from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = (article_tag.getText())
    article_texts.append(article_text)
    article_link = (article_tag.get("href"))
    article_links.append(article_link)

article_score = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

# Finding the largest upvote
largest_number = max(article_score)
largest_index = article_score.index(largest_number)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_score[largest_index])

# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("a"))
