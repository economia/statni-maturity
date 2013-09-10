#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from geopy import geocoders
import time
from sys import exit
import sys

ajdy = 0

f = open("ssRejstrikCoded_opravy2.csv", 'w')

with open("ssRejstrik_opravy2.csv", "rb") as csvfile:
	celler = csv.reader(csvfile, delimiter=";", quotechar='"')
	for line in celler:
		ajdy = ajdy + 1
		g = geocoders.GoogleV3()
		y = geocoders.Yahoo('JRzWhaPV34H4SIgp_XjoYtfMlbB9tdZ4AQ_UU3OZ.Iy2WFw0ABQJLYuPVppIolfQ')
		try:
			lat = g.geocode(line[1], exactly_one=False)[0][1][0]
			lng = g.geocode(line[1], exactly_one=False)[0][1][1]
		except:
			try:
				time.sleep(1)
				lat = g.geocode(line[1], exactly_one=False)[0][1][0]
				lng = g.geocode(line[1], exactly_one=False)[0][1][1]
			except:
				try:
					time.sleep(3)
					lat = g.geocode(line[1], exactly_one=False)[0][1][0]
					lng = g.geocode(line[1], exactly_one=False)[0][1][1]
				except:
					try:
						time.sleep(5)
						lat = g.geocode(line[1], exactly_one=False)[0][1][0]
						lng = g.geocode(line[1], exactly_one=False)[0][1][1]
					except:
						try:
							time.sleep(10)
							lat = g.geocode(line[1], exactly_one=False)[0][1][0]
							lng = g.geocode(line[1], exactly_one=False)[0][1][1]
						except:
							lat = ""
							lng = ""
							print("Chyba pri geokodovani u hodnoty " + str(ajdy))
							print "Chyba:", sys.exc_info()[0]
		f.write(str(line[0]) + ';' + str(lat) + ';' + str(lng) + '\n')

f.close()