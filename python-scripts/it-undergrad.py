from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

courses = []

def getCourses(courseno):
    url = f'https://handbook.uts.edu.au/courses/c{courseno}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    courseinfo = soup.find('div', class_='ie-images')
    title = courseinfo.find('h1').text
    if title != "Page Not Found":
        num = title.split()[0]
        name = title.partition(' ')[2]
        maj = courseinfo.find('h1').find_next_sibling('em').text
        entry = "Course"
        area = "IT"
        cp = soup(text=re.compile('Load credit points'))
        level = "Undergraduate"
        description = courseinfo.find('h2').find_next_sibling('p').text
        courses.append({
                        'num': num, 
                        'name': name,
                        'cp': cp,
                        'maj': maj,
                        'level': level,
                        'entry': entry,
                        'area': area,
                        'url': url,
                        'description': description
                        })
    return

for x in range(10143, 10149):
    getCourses(x)
    
df = pd.DataFrame(courses)
df.to_json('it-undergrad.json', orient= 'records')