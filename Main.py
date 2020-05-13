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

if (site == 1):
	print("MD Computer selected")
	while True:
		try:
			comp = int(input("\nEnter {} for CPU {} or for GPU {} for RAM price list: ".format("'1'", "'2'", "'3'")))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	if (comp == 1):
		print("CPU selected")
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
	if (comp == 2):
		print("GPU selected")
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
	if (comp == 3):
		print("RAM selected")
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

elif (site == 2):
	print("PrimeABGB selected")
	while True:
		try:
			comp = int(input("\nEnter {} for CPU {} for GPU {} for RAM price list: ".format("'1'", "'2'", "'3'")))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue
		else:
			break
	if (comp == 1):
		print("CPU selected")
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
	if (comp == 2):
		print("GPU selected")
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
	if (comp == 3):
		print("RAM selected")
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

