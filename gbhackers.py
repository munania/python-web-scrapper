# from urllib.request import urlopen as uReq
import csv
import requests
from bs4 import BeautifulSoup as soup

url_list = []
my_url = 'https://gbhackers.com/category/ransome/'
page_url = requests.get(my_url)

# html parsing
page_soup = soup(page_url.content, "lxml")

filename = "Products.csv"
f = csv.writer(open(filename, 'w'))

f.writerow(["CONTENT_TITLE", "CONTENT_DESCRIPTION", "CONTENT_LINK"])

# Grab each container
containers = page_soup.find_all('div', class_='td_module_10')

for container in containers:
# Get the post title
	page_title = container.h3.text
	
# Get the post description
	description_container = container.find('div', class_='td-excerpt')
	description_prod = description_container.text

# Get The post link
	link = container.div.a['href']
	
	# print("TITLE:")
	# print(page_title)
	# print("DESCRIPTION:")
	# print(description_prod)
	# print("LINK:")
	# print(link)
	# print()
	url_list.append(link)

	f.writerow([page_title,description_prod, link])


# for url in url_list:
# 	print(url)
# 	print()