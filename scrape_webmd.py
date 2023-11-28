# scrape links to all webmd health topics
import bs4
import requests
import pandas as pd

# get all links to health topics
init_link = "https://www.webmd.com/a-to-z-guides/health-topics?pg="
links = []
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

for letter in list(map(chr, range(97, 123))):
    link = init_link + letter
    page = requests.get(link, headers=headers)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    topics = soup.find('ul', class_='az-index-results-group-list').find_all('li')
    for topic in topics:
        links.append(topic.find('a')['href'])
# remove inproper links
cleaned_links = []
for link in links:
    if link.startswith('https://www.webmd.com/'):
        cleaned_links.append(link)

# convert clean links to dictionary format { title: title, url: link}
cleaned_links = list(dict.fromkeys(cleaned_links))
cleaned_links = [{'title': link.split('/')[-1], 'url': link} for link in cleaned_links]
cleaned_links = pd.DataFrame(cleaned_links)

# convert tiles to title case and remove dashes
cleaned_links['title'] = cleaned_links['title'].str.replace('-', ' ')

print(cleaned_links)

# save to json
cleaned_links.to_json('webmd_links.json', orient='records')

from doc import Documents
import json
import pickle

# read webmd_links.json
with open("webmd_links.json", "r") as f:
    sources = json.load(f)

documents = Documents(sources)

# save documents
with open("docs.pkl", "wb") as f:
    pickle.dump(documents, f)