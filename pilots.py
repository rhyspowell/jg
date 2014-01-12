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

def scrape_pilots():
	for link in soup.find_all('a'):
		pilot = []
		pilot.append(link.get('href'))
		for p in pilot:
			if p.startswith('/database/pilot/'):
				s = p.rsplit('/')
				t = s[3].split('.')
				pilots.append(t[0])

def query_pilots():
	database_pilots = db.cursor()
	cursor.execute('select * from pilots')
	for row in cur.fetchall():
		print row


query_pilots()