from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

newva = []

def getSubjects(subjectno):
    url = f'https://handbook.uts.edu.au/subjects/{subjectno}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    for item in subjectinfo:
        subject = {
        'title': subjectinfo.find('h1').text,
        'info':  "".join([em.text for em in subjectinfo.find_all('em')])
        # 'description': subjectinfo.find('h3').next_element.next_element.next_element.text
        }
        newva.append(subject)
    return

# getSubjects('31251')
# print(subjectinformation)

for x in range(31251, 31252):
    getSubjects(31251)

df = pd.DataFrame(newva)
df.to_json('subjects.json')