from bs4 import BeautifulSoup
import requests
import pandas as pd

# Bypass basic web scraping protection
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjectlist = []

# url = 'https://handbook.uts.edu.au/subjects/31251.html'
url = 'https://www.handbook.uts.edu.au/comm/lists/numerical.html'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())

courseArea = soup.find('div', class_='ie-images')
subjects = courseArea.find_all('a')

# print(subjects)

# title = content.find('h1').get_text()

for item in subjects:
    subject = {
        'title' : item['href'],
        'subjectno' : item.text
    }
    subjectlist.append(subject)

print(subjectlist)

# print(title)
# print(soup.title.text)