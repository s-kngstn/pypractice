import requests
from bs4 import BeautifulSoup
# import lxml <-- consider using lxml is youre given an error telling you your parser is not working 


response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# article_tag = soup.find(name="a", class_="storylink") #<-- Will find the first instance with 'find'
articles = soup.find_all(name="a", class_="storylink") #<-- finds all instances
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# upvote = int(article_upvotes[0].split()[0])
# print(upvote)
most_upvotes = max(article_upvotes)
# print(most_upvotes)
# find index of largest number
most_votes_index = article_upvotes.index(most_upvotes)
print(most_votes_index)
print(article_texts[most_votes_index])
print(article_links[most_votes_index])
print(article_upvotes[most_votes_index])

# article_text = soup.select(selector=".storylink")[0].string
# yc_headline = soup.select(selector=".storylink")

# num = 0
# for headline in yc_headline:
#     articles = yc_headline[num].get("href")
#     num += 1
#     print(articles)







# --------------- USING BEAUTIFUL SOUP - BASICS USING LOCAL HTML FILE -------------------------------- # 
# 
# # with open("website.html", mode="r") as html: 
#       contents = html.read() 
# soup = BeautifulSoup(contents, "html.parser") 
#       print(soup.title)
#       print(soup.title.name)
# # print(soup.title.string) # 
# # print(soup.prettify()) # 
# # print(soup.a) # #a print(soup.li) 
# # all_anchor_tags = soup.find_all(name="a") # 
# for tag in all_anchor_tags: 
#    print(tag.getText())     
#    print(tag.get("href"))
# heading = soup.find(name="h1", id="name")
# print(heading.string)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)

# select_class = soup.select(selector=".heading")
# print(select_class)

