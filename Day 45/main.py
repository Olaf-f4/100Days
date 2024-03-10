from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://news.ycombinator.com/'
soup = BeautifulSoup(requests.get(BASE_URL, 'html.parser').text, 'html.parser')
td = soup.find('td', class_='title')


title = ''
for x in soup.find_all('td', class_='title'):
    for y in x:
        if y.find_all('a') is None:
            pass
        else:

    # print(x.get('href'), string)


    # if string[0].isdigit():
    #     pass
    # else:
    #     title = x



