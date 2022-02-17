from bs4 import BeautifulSoup
import requests
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
        subno = int(title.split()[0])
        subname = title.partition(' ')[2]
        maj = detailsubjectinfo.find('h1').find_next_sibling('em').text.replace('UTS: Information Technology: ', '')
        entry = "subject"
        area = "IT"
        info =  "".join([em.text for em in subjectinfo.find_all('em')])
        cp = int(subjectinfo.find('h1').find_next_sibling('em').text.replace('cp', ''))
        level = subjectinfo.find('h3').find_previous_sibling('em').text
        description = subjectinfo.find('h3').find_next_sibling('p').text + subjectinfo.find('h3').find_next_sibling('p').find_next_sibling('p').text
        subjects.append({
                        'subno': subno, 
                        'subname': subname,
                        'cp': cp,
                        'maj': maj,
                        'level': level,
                        'entry': entry,
                        'area': area,
                        'url': url,
                        'description': description,
                        'info': info
                        })
    return

for x in range(31251, 31258):
    getSubjects(x)

# print(subjects)

df = pd.DataFrame(subjects)
# , index = ['name', 'info', 'description', 'entry', 'area']
# df.to_excel('it-subjects.xlsx', index=False)
df.to_json('it-subjects3.json', orient= 'records')