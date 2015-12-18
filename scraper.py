# https://github.com/ireapps/first-web-scraper/blob/master/scrapers/crime/scrape.py
import csv
import requests
import time
from BeautifulSoup import BeautifulSoup


url = 'http://www.footballoutsiders.com/stats/fplus'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
tbody = soup.find('tbody')

list_of_rows = []
for row in tbody.findAll('tr'):
    list_of_cells = []
    # skip mixed-in header rows
    if not row.findAll('td')[0].text == 'Team':
        for cell in row.findAll('td'):
            list_of_cells.append(cell.text)
        list_of_rows.append(list_of_cells)

# get Outsiders
outfile = open('outsiders.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
outfile.close()
# ... and we crack it right back open again ...
reader = csv.reader(open('outsiders.csv'))
try:
    for team, conference, record, f_plus, f_plus_rank, last_week, change, s_and_p_plus, s_and_p_plus_rank, fei, fei_rank in reader:
        print team, f_plus_rank
except ValueError, err:
    print err

# get Sagarin from massey
massey_url = 'http://www.masseyratings.com/cf/compare.csv'
massey_composite = requests.get(massey_url)
massey_csv_raw = massey_composite.content
massey_read = csv.reader(massey_csv_raw)
for massey_row in massey_read:
    print massey_row
