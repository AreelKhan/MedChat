# download all the htmls from docs.json
# documents.load()
import requests
import json

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

with open('source/docs.json') as f:
    docs = json.load(f)

for doc in docs:
    r = requests.get(doc['url'], headers=headers)
    with open(f"source/htmls/{doc['url'].split('/')[-1]}.html", "w") as f:
        f.write(r.text)