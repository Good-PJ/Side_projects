import requests
from bs4 import BeautifulSoup
import json
import random
import time

for i in range(0, 744, 12):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}'
    q = requests.get(url)
    result = q.content
    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all(class_='bt-slide-content')
    
    persons_url_list = []
    for person in persons:
        link = person.find('a').get('href')
        persons_url_list.append(link)
        
    with open('persons_url_list.txt', 'a') as file:
        for line in persons_url_list:
            file.write(f'{line}\n')  
# all links in file


with open('persons_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    
    data_dict = []
    
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_="bt-biografie-name").find('h3').text
        person_name_co = person.strip().split(',')
        person_name = person_name_co[0]
        person_co = person_name_co[1]
        
        social_net = soup.find_all(class_='bt-link-extern')
        
        social_net_links = []
        for unit in social_net:
            social_net_links.append(unit.get('href'))
        
        data= {
            'person_name': person_name,
            'person_co': person_co,
            'social_net': social_net_links
        }
        
        count += 1
        print(f'{count}: {line} is done')
    
        data_dict.append(data)
        
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
            
        time.sleep(random.randrange(2, 5))