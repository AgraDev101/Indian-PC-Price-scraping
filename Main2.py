from bs4 import BeautifulSoup
import requests
import io
import pandas as pd
from fake_useragent import UserAgent

def prime_gpu(a,b):
	return print(a+b)

def prime_cpu(a,b):
	return print(a+b)

def prime_ram(a,b):
	return print(a+b)

def md_gpu(a,b):
	return print(a+b)

def md_cpu(a,b):
	return print(a+b)

def md_ram(a,b):
	return print(a+b)


while True:
    try:
        site = int(input("Enter {} for MD Computer {} for PrimeABGB: ".format("'1'", "'2'")))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

while True:
	try:
		comp = int(input("Enter {} for CPU or {} for GPU or{} for RAM price list: ".format("'1'", "'2'", "'3'")))
	except ValueError:
		print("Sorry, I didn't understand that.")
		continue
	else:
		break

if (site == 1 and comp == 1):
	print("MD Computer and CPU price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_cpu(page_from, page_to)

elif (site == 1 and comp == 2):
	print("MD Computer and GPU price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_gpu(page_from, page_to)

elif (site == 1 and comp == 3):
	print("MD Computer and RAM price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	md_ram(page_from, page_to)

elif (site == 2 and comp == 1):
	print("PrimeABGB and CPU price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_cpu(page_from, page_to)

elif (site == 2 and comp == 2):
	print("PrimeABGB and GPU price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_gpu(page_from, page_to)

elif (site == 2 and comp == 3):
	print("PrimeABGB and RAM price selected")
	while True:
		try:
			page_from = int(input("Starting page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	while True:
		try:
			page_to = int(input("Upto page(e.g., 1 or 2 etc): "))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	prime_ram(page_from, page_to)

else:
	print("Nothing selected")