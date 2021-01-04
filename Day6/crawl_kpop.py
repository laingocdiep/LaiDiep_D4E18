from requests import get
from bs4 import BeautifulSoup
import pyexcel

response =  get('https://dbkpop.com/db/all-k-pop-idols?fbclid=IwAR1z-P5Lcu6JxprgzxJ3aUuW5CrYHARPAAgDSIfkaPCv5v26VjFM9-31bK4')
# file = open('kpop.html', 'w', encoding='utf-8')
content_html = BeautifulSoup(response.text)
# file.write(content_html.prettify())

table_html = content_html.find('table', {'id': 'table_1'})

print(table_html)