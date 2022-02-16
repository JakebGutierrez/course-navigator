from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjectinfo = []

def subjectPage(page):
    url = 'https://www.handbook.uts.edu.au/subjects/{page}.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    courseArea = soup.find('div', class_='ie-images')
    subjects = courseArea.find_all('a')

    # print(subjects)

    # title = content.find('h1').get_text()

    for item in subjects:
        subject = {
            'title' : item['href'],
            'subjectno' : item.text
        }
        subjectinfo.append(subject)

# print(title)
# print(soup.title.text)