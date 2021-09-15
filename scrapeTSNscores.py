import requests
from bs4 import BeautifulSoup

#get the data from the website
data = requests.get('https://www.tsn.ca/')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#get data simply by looking for each <tr>
data =[]
for widget in soup.find_all('widgets-bms-scores'):
    print(widget)
