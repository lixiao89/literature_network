import json

with open("urls.json") as f:
    urls = json.load(f)

if isinstance(urls, list) and len(urls) > 0 and isinstance(urls[0], dict):
    urls = [x['url_citations'] for x in urls]

with open("extract.json", "wb") as out:
    json.dump(urls,out)