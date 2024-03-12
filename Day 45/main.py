from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://news.ycombinator.com/'
soup = BeautifulSoup(requests.get(BASE_URL).text, 'html.parser')
tbody = soup.find('table', id='hnmain')


def high_pop():

    score_list = {}
    for score in tbody.find_all('span', class_='score'):

        # Get User ID
        user_id = score.get('id')
        r = user_id.replace('score_', '')

        # Get User Score - Remove 'points' from word leaving just points
        strip_score = score.get_text().split()
        for word in strip_score:
            if 'points' in word:
                strip_score.remove(word)

        user_score = 0
        for x in strip_score:
            user_score = int(x)

        # adding user_id and points to dictionary for further call
        score_list[r] = user_score

    for loser_id, loser_score in score_list.copy().items():
        if loser_score < 300:
            del score_list[loser_id]

    # if tbody.find_all('span', class_='score'):
    #     print(tbody.find_all('span', class_='score'))

    return score_list


def query(posts_dictionary):
    top_posts = {}
    for x in posts_dictionary.keys():

        link = ''
        for post in tbody.find_all('tr', class_='athing', id=f'{x}'):
            for z in post.find_all('a', href=True):
                if z['href'].startswith('http'):
                    link = z['href']

            post_text = post.text.split()
            for y in post_text:
                if '.' in y:
                    post_text.remove(y)

            finished_posts = ' '.join(post_text)
            top_posts[link] = finished_posts

    return top_posts


query(high_pop())
