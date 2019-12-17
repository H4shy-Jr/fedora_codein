import requests as r

from bs4 import BeautifulSoup

l = ['google','facebook','microsoft','telenet','twitter','discord','mozilla']

url = "https://viewdns.info/reversewhois/?q="

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

for i in l:
	# print(url)
	# print(r.post(url, data).text)

	s = url+i
	# print("url is ",s)
	m = (r.post(url = s,headers = headers).text)
	# print(m)
	soup = BeautifulSoup(m)

	table = soup.find('table', attrs = {'border':'1'})

	output_rows = []
	for table_row in table.findAll('tr'):
	    columns = table_row.findAll('td')
	    output_row = []
	    for column in columns:
	        output_row.append(column.text)
	    output_rows.append(output_row)

	# print("Domain names:")

	for j in output_rows:
		if j[0] == 'Domain Name':
			print(j[0],'of',i)
			print('\n')
			continue
		print(j[0])
	print('\n')