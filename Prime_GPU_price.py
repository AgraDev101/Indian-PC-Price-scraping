from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent

def Prime_GPU(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/page/"
		res = requests.get((base_url + str(page) + "/"), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "product-innfo"}):
			d = {}
			try:
				name = info.find("h3").text
				d["GPU_Name"] = name
			except:
				d["GPU_Name"] = None
				
			try:
				price = info.find("ins").text
				d["Price"] = price
			except:
				d["Price"] = None

			data.append(d)

	print("Total " + str(len(data)) + " entries found")
	df = pd.DataFrame(data)
	df.to_csv("PrimeABGB_GPU_price.csv")

Prime_GPU(1, 3)