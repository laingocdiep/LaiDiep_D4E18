from requests import get
from bs4 import BeautifulSoup
import pyexcel

response = get('https://dantri.com.vn/')

# file = open('dantri.html', 'w', encoding='utf-8')
# file.write(response.text)

# w = write
# as can be seen in html page: <meta charset="utf-8">

# load html to bs4
content_html = BeautifulSoup(response.text)

# find ul tag that contains data
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
    
pyexcel.save_as(dest_file_name='dantri.xls', records=data)      # luu vao file co name la 'dantri.xls', du lieu la data



