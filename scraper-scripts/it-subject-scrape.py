from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjects = []

def getSubjects(subjectno):
    url = f'https://handbook.uts.edu.au/subjects/details/{subjectno}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    title = subjectinfo.find('h1').text
    docType = "subject"
    area = "IT"
    if title != "Page Not Found":
        info =  "".join([em.text for em in subjectinfo.find_all('em')])
        description = subjectinfo.find('h3').find_next_sibling('p').text + subjectinfo.find('h3').find_next_sibling('p').find_next_sibling('p').text
        subjects.append([title, info, description, docType, area])
    return

for x in range(31251, 31258):
    getSubjects(x)

# print(subjects)

df = pd.DataFrame(subjects, columns = ['name', 'info', 'description'])
df.to_excel('it-subjects.xlsx', index=False)
# df.to_json('it-subjects.json')