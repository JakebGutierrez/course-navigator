from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

subjects = []

def getSubjects(subjectno):
    url = f'https://handbook.uts.edu.au/subjects/{subjectno}'
    detailurl = f'https://handbook.uts.edu.au/subjects/details/{subjectno}'
    r = requests.get(url, headers=headers)
    detailr = requests.get(detailurl, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    detailsoup = BeautifulSoup(detailr.text, 'lxml')
    subjectinfo = soup.find('div', class_='ie-images')
    detailsubjectinfo = detailsoup.find('div', class_='ie-images')
    title = subjectinfo.find('h1').text
    if title != "Page Not Found":
        num = title.split()[0]
        name = title.partition(' ')[2]
        maj = detailsubjectinfo.find('h1').find_next_sibling('em').text.replace('UTS: Information Technology: ', '')
        entry = "Subject"
        area = "Business"
        info =  "".join([em.text for em in subjectinfo.find_all('em')])
        cp = "Credit Points: " + subjectinfo.find('h1').find_next_sibling('em').text.replace('cp', '')
        level = subjectinfo.find('h3').find_previous_sibling('em').text
        description = subjectinfo.find('h3').find_next_sibling('p').find_next_sibling('p').text
        subjects.append({
                        'num': num, 
                        'name': name,
                        'cp': cp,
                        'maj': maj,
                        'level': level,
                        'entry': entry,
                        'area': area,
                        'url': detailurl,
                        'description': description,
                        'info': info
                        })
    return

for x in range(20501, 20505):
    getSubjects(x)

df = pd.DataFrame(subjects)
df.to_json('business-subjects.json', orient= 'records')