from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent
from mdcomputers_data import MD_CPU
from mdcomputers_data import MD_GPU
from mdcomputers_data import MD_RAM

def prime_gpu(a,b):
	print("\nscraping...")
	return print(a+b)

def prime_cpu(a,b):
	print("\nscraping...")
	return print(a+b)

def prime_ram(a,b):
	print("\nscraping...")
	return print(a+b)

def md_gpu(a,b):
	print("\nscraping...")
	return print(a+b)

def md_cpu(page_from, page_to):
	print("\nscraping...")
	MD_CPU(page_from, page_to)

def md_ram(a,b):
	print("\nscraping...")
	return print(a+b)


while True:
    try:
        site = int(input("Enter {} for MD Computer or {} for PrimeABGB: ".format("'1'", "'2'")))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

while True:
	try:
		comp = int(input("Enter {} for CPU or {} for GPU or {} for RAM price list: ".format("'1'", "'2'", "'3'")))
	except ValueError:
		print("Sorry, I didn't understand that.")
		continue
	else:
		break

if (site == 1 and comp == 1):
	print("\nMD Computer and CPU price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_cpu(page_from, page_to)

elif (site == 1 and comp == 2):
	print("\nMD Computer and GPU price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_gpu(page_from, page_to)

elif (site == 1 and comp == 3):
	print("\nMD Computer and RAM price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_ram(page_from, page_to)

elif (site == 2 and comp == 1):
	print("\nPrimeABGB and CPU price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_cpu(page_from, page_to)

elif (site == 2 and comp == 2):
	print("\nPrimeABGB and GPU price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_gpu(page_from, page_to)

elif (site == 2 and comp == 3):
	print("\nPrimeABGB and RAM price selected")
	while True:
		try:
			page_from = int(input("\nStarting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
			page_to += 1
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_ram(page_from, page_to)

else:
	print("Nothing selected")