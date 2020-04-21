import requests

from bs4 import BeautifulSoup

import csv

url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp'

headers = {'User-Agent' : 'Mozilla-5.0'}

resp = requests.get(url,headers = headers)

# print (resp.status_code)



soup = BeautifulSoup(resp.text,'html.parser')

def nifty_value(soup):
	return (soup.find('table').span.text)

table_find = soup.find('table', id = 'octable')

table_body = table_find.find('tr')

# print (table_find.prettify())

# rws = table_body.find_all('th')
# print (rws[0].text)

# print (rws)

final_list = []

# print (table_body)

for rowes in table_find.find_all('tr'):
	inter_list = []

	# print (rowes)

	for colum in rowes.find_all('th'):
		# print (colum)
		inter_list.append(colum.text)

	if len(inter_list) != 0:

		inter_list = [i.upper() for i in inter_list]

		final_list.append(inter_list)


# print (final_list)


# def extract_data(ref_text_row,ref_text_col,list_name):
# 	table_body = table_find.find(ref_text_row)

# print (final_list)

final_list1 = []

for rowes in table_find.find_all('tr'):
	inter_list = []

	# print (rowes)

	for colum in rowes.find_all('td'):
		# print (colum)
		inter_list.append(colum.text)

	if len(inter_list) != 0:

		inter_list = [i.strip() for i in inter_list]


		final_list1.append(inter_list)


# print (final_list1)

input_csv_data = final_list[1:] + final_list1

# print (input_csv_data)



with open('option_data.csv','w') as file1:

	file1_writer = csv.writer(file1)

	for i in input_csv_data:
		# print (i)
		file1_writer.writerow(i)


print (nifty_value(soup))