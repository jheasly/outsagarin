# https://github.com/ireapps/first-web-scraper/blob/master/scrapers/crime/scrape.py
import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.footballoutsiders.com/stats/fplus'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
tbody = soup.find('tbody')

list_of_rows = []
for row in tbody.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open('./outsiders.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
