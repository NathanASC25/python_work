import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

url = input('Enter Url: ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

elements = soup('li')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print('Retrieving:', url)
string = 'href="(.*)"'
while (count > 0):
    element = elements[position - 1]
    link = re.findall(string, element.decode())
    print('Retrieving:', link[0])
    html = urllib.request.urlopen(link[0])
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup('li')
    count -= 1
