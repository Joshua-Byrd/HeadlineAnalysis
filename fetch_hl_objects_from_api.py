from newsapi import NewsApiClient
import json
import os

# NewsAPI setup
newsapi_key = "8aaee90f51a245999fc29a980d1ce20c" 
newsapi = NewsApiClient(api_key=newsapi_key)

# paths
merged_sources_path = "./data/raw/merged_sources.json"
headline_objects_path = "./data/raw/headline_objects.json"

# get source ids from the merged sources and convert to comma-separated string
with open(merged_sources_path, "r") as file:
    sources = json.load(file)

source_str = ",".join([value["id"] for key, value in sources.items()])

# fetch new headline objects using source list
headline_objects = newsapi.get_everything(sources=source_str, language='en')
new_articles = headline_objects.get("articles", [])

# load existing articles if the file is present
if os.path.exists(headline_objects_path):
    with open(headline_objects_path, "r") as file:
        existing_data = json.load(file)
        existing_articles = existing_data.get("articles", [])

else:
    existing_articles = []

# combine new and existing articles and deduplicate using url
combined_articles = {x["url"]: x for x in existing_articles}

for article in new_articles:
    combined_articles[article["url"]] =  article

# write back to file
with open(headline_objects_path, "w") as file:
    json.dump({"articles": list(combined_articles.values())}, file, indent=2)