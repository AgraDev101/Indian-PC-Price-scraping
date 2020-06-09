from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent
from datetime import date
from sys import stdout
import time


d1 = date.today().strftime("%d-%m-%Y")

def Prime_CPU(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://www.primeabgb.com/buy-online-price-india/cpu-processor/page/"
		res = requests.get((base_url + str(page) + "/"
		+"?pa-_stock_status=instock"
		), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "product-innfo"}):
			d = {}
			try:
				name = info.find("h3").text
				d["CPU_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["CPU_Name"] = None
				
			try:
				price = info.find("ins").text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				try:
					price = info.find("span","price").text
					d["Price"] = int(price.replace("₹", "").replace(",", ""))
				except:
					d["Price"] = None


			data.append(d)

			stdout.write("\r{}".format("Total " + str(len(data)) + " products added"))
			stdout.flush()

	stdout.write("\n")		
	df = pd.DataFrame(data)
	df.to_csv("PrimeABGB_CPU_price_{}.csv".format(d1), index = False)

def Prime_GPU(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/page/"
		res = requests.get((base_url + str(page) + "/"
		+"?pa-_stock_status=instock"
		), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "product-innfo"}):
			d = {}
			try:
				name = info.find("h3").text
				d["GPU_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["GPU_Name"] = None
				
			try:
				price = info.find("ins").text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				try:
					price = info.find("span","price").text
					d["Price"] = int(price.replace("₹", "").replace(",", ""))
				except:
					d["Price"] = None

			data.append(d)

			stdout.write("\r{}".format("Total " + str(len(data)) + " products added"))
			stdout.flush()
			
	stdout.write("\n")
	df = pd.DataFrame(data)
	df.to_csv("PrimeABGB_GPU_price_{}.csv".format(d1), index = False)

def Prime_RAM(page_from, page_to):
	data = []
	for page in range(page_from, page_to, 1):
		ua = UserAgent()
		base_url = "https://www.primeabgb.com/buy-online-price-india/ram-memory/page/"
		res = requests.get((base_url + str(page) + "/"
		+"?pa-_stock_status=instock"
		), headers={'User-Agent': ua.chrome})
		cont = res.content
		soup = BeautifulSoup(cont, "html.parser")
		
		for info in soup.find_all("div", {"class", "product-innfo"}):
			d = {}
			try:
				name = info.find("h3").text
				d["RAM_Name"] = str(name.replace("®", "").replace("™", ""))
			except:
				d["RAM_Name"] = None
				
			try:
				price = info.find("ins").text
				d["Price"] = int(price.replace("₹", "").replace(",", ""))
			except:
				try:
					price = info.find("span","price").text
					d["Price"] = int(price.replace("₹", "").replace(",", ""))
				except:
					d["Price"] = None

			data.append(d)

			stdout.write("\r{}".format("Total " + str(len(data)) + " products added"))
			stdout.flush()
			
	stdout.write("\n")
	df = pd.DataFrame(data)
	df.to_csv("PrimeABGB_RAM_price_{}.csv".format(d1), index = False)