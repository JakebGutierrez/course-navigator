from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjects = []

def getSubjects(subjectno):
    url = f'https://handbook.uts.edu.au/courses/c{subjectno}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    title = subjectinfo.find('h1').text
    entry = "undergrad"
    area = "IT"
    if title != "Page Not Found":
        # info =  "".join([em.text for em in subjectinfo.find_all('em')])
        courseprogram = "".join([table.text for table in subjectinfo.find_all('table')])
        description = subjectinfo.find('h2').find_next_sibling('p').text
        subjects.append([title, courseprogram, description, entry, area])
    return

for x in range(10143, 10149):
    getSubjects(x)

# print(subjects)

df = pd.DataFrame(subjects, columns = ['name', 'courseprogram', 'description', 'entry', 'area'])

# df.to_excel('it-undegrad.xlsx', index=False)
df.to_json('it-undergrad.json')