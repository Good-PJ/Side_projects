import requests
from bs4 import BeautifulSoup

link = 'https://...'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
txt = soup.find('ol')
txt = str(txt)
txt = txt.replace('</li></ol>', '')
txt = txt.replace('<ol><li>', '')
txt = txt.split('</li><li>')
with open('file.txt', 'w', encoding='utf-8') as f:
    for line in txt:
        f.write('***' + '\n' + line + '\n')
<<<<<<< HEAD
<<<<<<< HEAD
=======
print(txt)
>>>>>>> 7957369 (Rename Parce.py to Project_01/Parce.py)
=======
>>>>>>> 65ad88b (Parcing-file correction)
