import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
string = ">(.*)<"
total = 0
for tag in tags:
    validNums = re.findall(string, tag.decode())
    for validNum in validNums:
        total += int(validNum)
print(total)
