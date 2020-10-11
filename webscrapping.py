import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.fxautotrade.com/systems/rambo/1869026'

response = requests.get(url)

soup = BeautifulSoup(response.text,
'html.parser')

# el = soup.body
# el = soup.find('tr')
table_body = soup.select('#openTrades')[0].find('tbody')
rows = table_body.find_all('tr')

with open('OpenTrades.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['OpenDate', 'Symbol', 'Action', 
			'Lots','OpenPrice', 'SL', 
			'TP', 'Profit', 'Pips', 
			'Swap', 'Gain']
	csv_writer.writerow(headers)
	
	for row in rows:
		cols=row.find_all('td')
		cols=[x.text.strip() for x in cols]
		print(cols)
		csv_writer.writerow(cols)


# print(el)

