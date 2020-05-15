from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent


def MD_CPU(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://mdcomputers.in/processor?page="
		res = requests.get((base_url + str(page)), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "right-block right-b"}):
			d = {}
			try:
				name = info.find("a").text
				d["CPU_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["CPU_Name"] = None
			
			try:
				price = info.find("span", {"class", "price-new"}).text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				d["Price"] = None
			
			data.append(d)

	print("Total " + str(len(data)) + " entries found")
	df2 = pd.DataFrame(data)
	df2.to_csv("MDComputers_CPU_price.csv", index = False)

def MD_GPU(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://mdcomputers.in/graphics-card?page="
		res = requests.get((base_url + str(page)), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "right-block right-b"}):
			d = {}
			try:
				name = info.find("a").text
				d["GPU_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["GPU_Name"] = None
			
			try:
				price = info.find("span", {"class", "price-new"}).text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				d["Price"] = None
			
			data.append(d)

	print("Total " + str(len(data)) + " entries found")
	df2 = pd.DataFrame(data)
	df2.to_csv("MDComputers_GPU_price.csv", index = False)

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
				d["RAM_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["RAM_Name"] = None
			
			try:
				price = info.find("span", {"class", "price-new"}).text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				d["Price"] = None
			
			data.append(d)

	print("Total " + str(len(data)) + " entries found")
	df2 = pd.DataFrame(data)
	df2.to_csv("MDComputers_RAM_price.csv", index = False)