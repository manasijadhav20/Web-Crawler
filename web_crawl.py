import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

html = urlopen('https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets')
bsobj = soup(html.read(),features="lxml")
print("List of Largest Recorded Music Markets from 2004-2019")
year = int(input("Enter Year: "))
if year == 2019:
	i = 1
elif year == 2018:
	i = 2
elif year == 2017:
	i = 3
elif year == 2016:
	i = 4
elif year == 2015:
	i = 5
elif year == 2014:
	i = 6
elif year == 2013:
	i = 7
elif year == 2012:
	i = 8
elif year == 2011:
	i = 9
elif year == 2010:
	i = 10
elif year == 2009:
	i = 11
elif year == 2008:
	i = 12
elif year == 2007:
	i = 13
elif year == 2006:
	i = 14
elif year == 2005:
	i = 15
elif year == 2004:
	i = 16
tbody = bsobj('table',{'class':'wikitable plainrowheaders sortable'})[i].findAll('tr')
xl = []
for row in tbody:
	cols = row.findChildren(recursive = False)
	cols = tuple(element.text.strip().replace('%','') for element in cols)
	xl.append(cols)
# xl = xl[1:-1]
print(xl)
xl = xl[1:-1]
# print(xl)

val= int(input("Want to insert data into database (0/1)? \n"))
if(val == 1):
	import pymysql
	scrap_db = pymysql.connect(host='localhost',user='root',password = "",db='web_crawler',port=3306)
	# prepare a cursor object using cursor() method
	cursor = scrap_db.cursor()

	mySql_insert_query = """INSERT INTO WIKI (RANKING, MARKET, RETAIL_VALUE, PHYSICAL,DIGITAL,PERFORMANCE_RIGHTS,SYNCHRONIZATION) 
	VALUES (%s, %s, %s, %s ,%s, %s, %s) """

	records_to_insert = xl
	cursor = scrap_db.cursor()
	cursor.executemany(mySql_insert_query, records_to_insert)
	scrap_db.commit()
	print(cursor.rowcount, "Record inserted successfully into WIKI table")

	# disconnect from server
	scrap_db.close()



	