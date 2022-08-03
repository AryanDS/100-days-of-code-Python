from bs4 import BeautifulSoup


with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 45/bs4-start/website.html") as file:
    contents =  file.read()

#print(contents)

#Creating a beautiful soup object
soup = BeautifulSoup(contents, 'html.parser')
#Will give the title tag complete
print(soup.title)
#will give the name of the title tag which is title 
print(soup.title.name)
#Will give the title string 
print(soup.title.string)

#indent the html file
print(soup.prettify())

#gives the first anchor tag
print(soup.a)

#gives the first li tag
print(soup.li)

#gives the first paragraph tag
print(soup.p)

#We can use find_all() to find all of the anchor tags, paragraphs etc, returns a list 

anchor_tags = soup.find_all(name='a')
print(anchor_tags)

#Gathering the text from the anchor_tag object
for tag in anchor_tags:
    print(tag.getText())
    #if we want to get the href from the anchor_tag
    print(tag.get("href"))

#Gathering the first h1 tag with the id name
heading = soup.find(name='h1', id='name')
print(heading.string)

#Gathering all the h3 which has a class heading 
heading_h3 = soup.find(name='h3', class_='heading')
print(heading_h3)
print(heading_h3.getText())

heading_h3 = soup.find_all(name='h3', class_='heading')
print(heading_h3)
for i in heading_h3:
    print(i.getText())

#What if we want to get the anchor tag which is embedded inside several tags
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
company_url = soup.select_one(selector="p a") 
print(company_url)
print(company_url.get("href"))   


#What if we want to select_ one using the id
name = soup.select_one(selector="#name")
print(name)

#using select method to get tags which has a class of heading, return a list
heading_ = soup.select(selector='.heading')
print(heading_)



####################################################
#Scrapping a live website using beautiful soup

import requests

response = requests.get("https://news.ycombinator.com/show")
yc_webpage = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.prettify())

#Get the first occurance 
article = soup.find(name="a", class_="titlelink")
print(article)
article_text = article.getText()

article_link = article.get("href")
print(article_link)

article_upvote = soup.find(name='span', id="score_32266086")
print(article_upvote.getText())

#What if we want all the occurances

articles = soup.find_all(name ='a', class_='titlelink')
article_texts=[]
article_links=[]
for article_tag  in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))


articles_upvotes =  soup.find_all(name='span', class_='score')
article_upvotes =[score.getText() for score in articles_upvotes]


print(article_texts)
print(article_links)
print(article_upvotes)

#Spliting the article_upvotes to only have int, 26 instead of 26 points

upvotes =[int(votes.split(" ")[0]) for votes in article_upvotes]
print(upvotes)

#Print out the story and link with the highest number of upvotes
highest_score_index =  upvotes.index(max(upvotes))
print(highest_score_index)
print(article_texts[highest_score_index])
print(article_links[highest_score_index])