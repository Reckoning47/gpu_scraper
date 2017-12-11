import csv
import requests
from bs4 import BeautifulSoup

#url = 'http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=desktop+graphics+cards&ignorear=0&N=100007709%204814&isNodeId=1'
url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=desktop+graphics+cards&ignorear=0&N=100007709%204814%204803%20600358543&isNodeId=1'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
table = soup.find("div", attrs={'class':'items-view is-grid'})

items = []

# Model
model = []
for itemName in table.findAll(attrs={"class" : "item-title"}):
	text3 = itemName.get_text()
	model.append(text3)

# Price
priceDollars = []
for price in table.findAll(attrs={"class" : "price-current"}):
	for dollarValue in price.findAll("strong"):
		text1 = dollarValue.get_text()
		for centValue in price.findAll("sup"):
			text2 = centValue.get_text()
			priceDollars.append(text1 + text2)
	# items.append(priceDollars)

zipped = zip(model, priceDollars)

print zipped

# Writing to File
outfile = open("./GPUScrape.csv","wb")
writer = csv.writer(outfile)
writer.writerows(zipped)