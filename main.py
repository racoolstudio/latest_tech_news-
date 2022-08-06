# # import the module
# from bs4 import BeautifulSoup
#
# # just incase html.parser is not working use lxml
# # import lxml
# with open('website.html') as web:
#     content = web.read()
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.title)
# # tag-name can be a,h1-h6,title...
# # we can get the first tag by saying soup.tagName
# # they are other attributes in the tag like name and string
# # print(soup.title.string)
# # print(soup.prettify()) prettify formats the html nicely
# # print(soup.find_all(name='a')) find_all gets all the tag name
# links = soup.find_all(name='a')
# # we can get anything like using the getText() method or the get('attribute name') method attribute name like 'href',
# # 'class' for link in links: print(link.get('href')) now lets find a specific item we are looking for h1 with id =
# for link in links:
#     print(link.get('href'))
# # 'name' heading = soup.find(name='h1', id='name') print(heading) find( any attribute, and it's value and class_ not
# # class lol )
# # Drilling our data
# # we use the selectors
# url = soup.select_one(selector='p a')  # which would return the first matching item while select would give us all
# # matching items
# # print(url.get('href')) in the selector property you can use anything just remember that global selector does not
# # usen a dot eg body but for class we use .class name and for id we use the #idname
#
#
# Gettin info from a live web site
from bs4 import BeautifulSoup
from requests import *

data = get('https://news.ycombinator.com/newest').text
soup = BeautifulSoup(data, 'html.parser')
news = [{
    'heading': i.string,
    'link': i.get('href'),
} for i in soup.find_all(name='a', class_='titlelink')]
votes = [j.string
         for j in soup.find_all(name='span', class_='score')]
# getting the length of the votes which is always always equal to the news length and adding the votes key to the
# news dictionary
for i in range(len(votes)):
    news[i]['votes'] = int(votes[i].split(' ')[0])
print(news)


def find_highest(dic):
    high = 0
    high_list = 0
    for i in dic:
        if i['votes'] > high:
            high = i['votes']
            high_list = i

    print(high_list)


find_highest(news)
