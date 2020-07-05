import requests
from bs4 import BeautifulSoup
import urllib

import time
count = 0
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
for i in range(0,11):
    link = 'https://e-hentai.org/g/1321349/d773ea475c/?p=' + str(i)
    r = requests.get(link, headers = headers)
    print ('现在爬取的是第', i, '页')
    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('div', class_="gdtm")
    for house in house_list:
        name = house.find('a')['href']
        nr = requests.get(name, headers=headers)
        soup = BeautifulSoup(nr.text, 'lxml')
        image=soup.find_all('img',id="img")
        src = image[0].get('src')
        print(src)
        urllib.request.urlretrieve(src, r'./img/'+str(count)+'.jpg')
        count = count+1
