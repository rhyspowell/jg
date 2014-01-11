#!/usr/bin/env python
# coding: latin-1

import requests
import bs4

page = requests.get('http://jumpgate-tri.org/database/view-all-pilots.html')
soup = bs4.BeautifulSoup(page.text)
pilots = []

for link in soup.find_all('a'):
	pilot = []
	pilot.append(link.get('href'))
	for p in pilot:
		if p.startswith('/database/pilot/'):
			s = p.rsplit('/')
			t = s[3].split('.')
			pilots.append(t[0])

for i in pilots:
	print i
