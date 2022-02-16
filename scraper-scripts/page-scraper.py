from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

url = 'https://handbook.uts.edu.au/subjects/31251.html'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
subjectinfo = soup.find('div', class_='ie-images')

title = subjectinfo.find('h1').text
# print(title)

info = "".join([em.text for em in subjectinfo.find_all('em')])
# print(info)

# description = subjectinfo.find_all('p')
# desc = description[+2].text
# description = subjectinfo.find('h3').find_next_sibling('p').find_next_sibling('p').text

description = subjectinfo.find('h3').next_element.next_element.next_element.text
# print(description)

subjectinformation = [title, info, description]

df = pd.DataFrame(subjectinformation)
df.to_excel('stackquestions.xlsx', index=False)

# print(subjectinformation)

# with open(f'{title}.txt', 'w') as file:
#     file.write(eminfolist)

# df = pd.DataFrame(eminfolist)
# df.to_excel('stackquestions.xlsx', index=False)


# for item in subjectinfo:
#     title = subjectinfo.find('h1').get_text()
#     print(title)