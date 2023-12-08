from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
with open("blank/index.html") as file:
    src = file.read()
    #print(src)
    
soup = BeautifulSoup(src, "lxml")

#поиск и вывод инфы со страницы
#title = soup.title
#print(title.string)

#выбор сверху вниз только одного 
#page_h1 = soup.find("h1")
#print(page_h1)

#выбор сверху вниз всех
page_h1 = soup.find_all("h1")
#print(page_h1)

#вывод результата поиска в текстовый формат 
for item in page_h1:
    print(item.text)
    
#выбор имени пользователя как текст
#username = soup.find("div", class_="user__name")
#for item in username:
#    print(item.text.strip())
#username = soup.find("div", class_="user__name").find("span").text
#print(username)
#выбор по словарю
not_birthday = soup.find("div", {"class": "user__name", "id": "test_id"}).find("span").text
print(not_birthday)
#выбор всей информации о пользователе
find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
#print(find_all_spans_in_user_info)

for item in find_all_spans_in_user_info:
    print(item.text)
#выбор всех ссылок на социальные сети    
social_links = soup.find(class_="social__networks").find("ul").find_all("a")
for item in social_links:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}:{item_url}")
#поиск родителей
#.find_parent() .find_parents()

post_div = soup.find(class_="post__text").find_parent("div", "user__post").text
print(post_div)

#user_ava = soup.find(class_="user__avatar").find("img")
#for item in user_ava:

images = soup.select('div img')

images_url = images[0]['src']

img_data = requests.get(images_url).content

with open('images/'+ input() +'.jpg', 'wb') as handler:

       handler.write(img_data)
