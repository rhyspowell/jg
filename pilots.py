#!/usr/bin/env python
# coding: latin-1

import requests
import bs4
import MySQLdb

page = requests.get('http://jumpgate-tri.org/database/view-all-pilots.html')
soup = bs4.BeautifulSoup(page.text)
pilots = []
conn = MySQLdb.connect (host = "localhost",
                        user = "root",
                        passwd = "sm00TH**",
                        db = "jumpgate")
cur = conn.cursor()
def scrape_pilots():
	for link in soup.find_all('a'):
		pilot = []
		pilot.append(link.get('href'))
		for p in pilot:
			if p.startswith('/database/pilot/'):
				s = p.rsplit('/')
				t = s[3].split('.')
				pilots.append(t[0])
	return pilots

def query_pilots():
	db_pilots = []	
	cur.execute('select * from pilots')
	for row in cur.fetchall():
		 db_pilots.append(row[1])
	return db_pilots

app_pilots = scrape_pilots()
db_pilots = query_pilots()
missing_pilots = set(app_pilots) - set(db_pilots)
if len(missing_pilots) > 0:
	#add_pilots(missing_pilots)
	for i in missing_pilots:
		print i
		cur.execute('insert into pilots(pilots_name) values("%s")' % i) 
		conn.commit()
