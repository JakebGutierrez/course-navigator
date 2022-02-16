from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjects = []

def getSubjects(tag):
    url = f'https://handbook.uts.edu.au/courses/{tag}.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    title = subjectinfo.find('h1').text
    if title != "Page Not Found":
        info =  "".join([em.text for em in subjectinfo.find_all('em')])
        courseprogram = "".join([table.text for table in subjectinfo.find_all('table')])
        subjects.append([title, info, courseprogram])
    return

getSubjects('c10460')
# print(subjects)

df = pd.DataFrame(subjects, columns = ['name', 'info', 'description'])
df.to_excel('subjects.xlsx', index=False)
# df.to_json('subjects.json')