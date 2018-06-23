from bs4 import BeautifulSoup
import requests
import re


soups = []  

# get soups for each year
for i in range(1776, 2019):
    # assumption is that each link is in https://www.thecrimson.com/sitemap/year format
    r = requests.get('https://www.thecrimson.com/sitemap/' + str(i)) 
    soups.append(BeautifulSoup(r.text, 'html.parser'))

links_by_day = []
# get links to each available day
for i in soups:
    for j in i.findAll('a', href=re.compile('/sitemap/')):
        links_by_day.append('https://www.thecrimson.com' + j['href'])

soups_by_day = []
## get soups to each available day
for i in links_by_day:
    r = requests.get(i) 
    soups_by_day.append(BeautifulSoup(r.text, 'html.parser'))

all_articles = []
# get links to every article
for i in soups_by_day:
    for j in i.findAll('a', href=re.compile('/article')):
        all_articles.append('https://www.thecrimson.com' + j['href'])

text_file = open("articles.txt", "w")
text_file.write("\n".join(all_articles))
text_file.close()