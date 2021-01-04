import pymysql
from requests import get
from bs4 import BeautifulSoup
import pyexcel

response = get('https://dantri.com.vn/')

content_html = BeautifulSoup(response.text)

ul_html = content_html.find('ul', {'class': 'dt-list'})
li_html = ul_html.find_all('li')

data = []

for i in range(len(li_html)):
    a_html = li_html[i].find('a')
    title = a_html.text.strip()      # add strip() just to remove spaces at the beginning and the end of the string
    link = a_html['href']
    data.append({
        'title': title,
        'link': link
    })

# connect to mysql
client = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'laingocdiep2002'
)

board =  client.cursor()

# create database
def create_db():
    board.execute('''
        CREATE DATABASE `dan_tri`
    ''')


# create table
def create_table():
    board.execute('''
        CREATE TABLE `dan_tri`.`headline`(
            title text(10000),
            link text(10000)
        )
    ''')


# insert row
for i in range(len(data)):
    title = data[i]['title']
    link = data[i]['link']
    board.execute(f'''
        INSERT INTO `dan_tri`.`headline`(
            title,
            link
        ) VALUE (
            '{title}',
            '{link}'
        )
    ''')
    print(f'saved {title}')





client.commit()

