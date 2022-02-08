from cgitb import html
from operator import delitem
import re
import requests
from bs4 import BeautifulSoup as BS

import csv

URL = 'https://www.mashina.kg/search/all/'
# HEADERS = {'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'} 
def get_html(url, params = None):
    response = requests.get(url)
    return response.text
    

def get_data(html):
    soup = BS(html, 'lxml')
    items = soup.find_all('div', class_="list-item list-label")

    # print(items)
    
    for cars in items:
        
        try:
            title = cars.find('h2', class_='name').text.strip()
        except:
            title = ''
        try:
            price = cars.find('p', class_='price').find('stong').text
        except:
            price = ''
        try:
            info1 = cars.find('p', class_="year-miles").text.strip()
        except:
            info1 = ''
        try:
            info2 = cars.find('p', class_="body-type").text.strip()
        except:
            info2 = ''
        try:
            info3 = cars.find('p', class_="volume").text.strip() 
        except:
            info3 = ''
        try:
            img = cars.find('img', class_='lazy-image').get('data-src')
        except:
            img = ''
 
        data = {
            'title': title,
            'price': price,
            'info1': info1,
            'info2': info2,
            'info3': info3,
            'img': img
        }
        write_csv(data)

def write_csv(data):
    with open('cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (
                data['title'],
                data['price'],
                data['info1'],
                data['info2'],
                data['info3'],
                data['img']
            )
        )

def main():
    for page in range(33):
        print(f'Парсинг {page + 1}  страницы...')
        url = 'https://www.mashina.kg/search/all/?page=2{page}'
        html = get_html(url)
        get_data(html)
        
main()