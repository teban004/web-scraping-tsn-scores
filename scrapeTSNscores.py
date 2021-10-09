import requests
from bs4 import BeautifulSoup
import sys

scoresWebsite = 'http://theapp/crsadmin/Default.aspx'
#get the real scores
scoresData = requests.get(scoresWebsite)

print("The response from", scoresWebsite, "is", scoresData)
print()
#load data into bs4
soup = BeautifulSoup(scoresData.text, 'html.parser')

#get data simply by looking for each <tr>
print("Getting data from", scoresWebsite)

# if the website responds with a status different than 200, the script will stop
if (scoresData.status_code != 200):
    print("The website returned the following response:", scoresData)
    print("The script will stop here.")
    sys.exit()

for div in soup.find('div', {'id': 'mainContentDiv'}):
    print(div)



###### NOW ON TSN WEBSITE ######
TSNwebsite = 'https://www.tsn.ca/'
#get the data displayed on TSN website
TSNdata = requests.get(TSNwebsite)

print("The response from", TSNwebsite, "is", TSNdata)

#load data into bs4
soup = BeautifulSoup(TSNdata.text, 'html.parser')

#get data simply by looking for each <tr>
print("Getting data from", TSNwebsite)
TSNdata =[]
for widget in soup.find_all('widgets-bms-scores'):
    print(widget)

