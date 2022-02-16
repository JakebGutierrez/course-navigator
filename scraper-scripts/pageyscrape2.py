from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjects = []

def getSubjects(subjectno):
    url = f'https://handbook.uts.edu.au/subjects/{subjectno}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    for item in subjectinfo:
        sub = {     
        'title': item.find('h1').text,
        'info':  "".join([em.text for em in item.find_all('em')]),
        'description': item.find_all('p')[+2].text
        }
        subjects.append(sub)
    return

getSubjects('31251')
print(subjects)

# for x in range(31251, 31258):
#     getSubjects(x)

# df = pd.DataFrame(subjects)
# df.to_json('subjects.json')

# df = pd.DataFrame(subjects)
# df.to_excel('subjects.xlsx', index=False)