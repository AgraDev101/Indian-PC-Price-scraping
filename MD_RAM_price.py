from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent


def MD_RAM(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://mdcomputers.in/memory?page="
		res = requests.get((base_url + str(page)), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "right-block right-b"}):
			d = {}
			try:
				name = info.find("a").text
				d["RAM_Name"] = name
			except:
				d["RAM_Name"] = None
			
			try:
				price = info.find("span", {"class", "price-new"}).text
				d["Price"] = price
			except:
				d["Price"] = None
			
			data.append(d)

	print("Total " + str(len(data)) + " entries found")
	df2 = pd.DataFrame(data)
	df2.to_csv("MDComputers_RAM_price.csv")