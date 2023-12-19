from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')  # Specify the parser, e.g., 'html.parser'
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup)
# print(soup.prettify())
#
# print(soup.a)
# print(soup.li)

# How to get hold of all the specify tag?
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# How to get hold of certain tag using the id tag?
# heading = soup.find(name='h1', id="name")
# print(heading)

# used class_ instead of class because it is a reserved keyword in Python
# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))
# print(section_heading.getText())

# Using CSS selector to find the specifics one
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)

hi = soup.find_all("a")
print(hi)