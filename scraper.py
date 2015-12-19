# https://github.com/ireapps/first-web-scraper/blob/master/scrapers/crime/scrape.py
import csv
import requests
import StringIO
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

massey_url = 'http://www.masseyratings.com/cf/compare.csv'
massey_composite = requests.get(massey_url)
massey_csv_raw = massey_composite.content
massey_f = StringIO.StringIO(massey_csv_raw)
massey_read = csv.reader(massey_f)
# for Team, Conf, WL, Rank, my_ean, Trimmed, my_median, StDev, ABC, ACU, AND, AP, ARG, ASH, ATC, BAS, BBT, BCM, BDF, BIH, BIL, BOB, BOW, BRN, BSS, BWE, CFP, CGV, CI, CMV, COF, COL, CPA, CPR, CSL, CTW, D1A, DCI, DES, DEZ, DII, DOI, DOK, DOL, DP, DUN, ENG, EZ, FEI, FMG, FPI, GBE, GLD, GRS, HAT, HEN, HKB, HNL, HOW, ISR, JNK, KAM, KEE, KEL, KEN, KH, KLK, KNT, KPK, KRA, LAZ, LOG, LSD, LSW, MAA, MAS, MCK, MDS, MEA, MGN, MJS, MOR, MRK, MVP, MvG, NOL, NUT, OSP, PAY, PCP, PGH, PIG, PIR, PPP, PTS, RBA, REW, RFL, RSL, RT, RTB, RTH, RTR, RUD, RWP, S&P, SAG, SEL, SFX, SOL, SOR, SP, SRC, STH, STU, TFG, TPR, TRP, TS, UCC, USA, WEL, WIL, WLK, WMR, WOB, WOL, WWP, BLNK in massey_read:
#     print Team
