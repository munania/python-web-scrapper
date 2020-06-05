import csv
import requests
from bs4 import BeautifulSoup as soup

my_url = 'https://gbhackers.com/it-services-giant-cognizant-hit-by-maze-ransomware-cyber-attack//'
page_url = requests.get(my_url)

filename = "post-content2.csv"
f = csv.writer(open(filename, "w", encoding = "utf8"))

f.writerow(["POST_TITLE","POST_CONTENT"])

# html parsing
page_soup = soup(page_url.content, "lxml")

containers = page_soup.find_all('article', class_='post')

container = containers[0]

content = container.find('div', class_='td-post-content')

page_content = content.find_all('p', class_='')

title = container.find('h1', class_='entry-title')

post_title = title.text.strip()
print(post_title)
print()

# f.writerow([post_title])

for posts in page_content:
	post = page_content[0].text
	final_post = posts.text.strip()
	print(final_post)
	print()

	f.writerow([post_title, final_post])