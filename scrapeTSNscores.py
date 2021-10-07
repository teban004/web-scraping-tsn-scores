import requests
from bs4 import BeautifulSoup

scoresWebsite = 'http://theapp/crsadmin/Default.aspx'
#get the real scores
scoresData = requests.get(scoresWebsite)

print("The response from", scoresWebsite, "is", scoresData);
print()

TSNwebsite = 'https://www.tsn.ca/'
#get the data displayed on TSN website
TSNdata = requests.get(TSNwebsite)

print("The response from", TSNwebsite, "is", TSNdata);

#load data into bs4
soup = BeautifulSoup(TSNdata.text, 'html.parser')

#get data simply by looking for each <tr>
print("Getting data from", TSNwebsite)
TSNdata =[]
for widget in soup.find_all('widgets-bms-scores'):
    print(widget)

