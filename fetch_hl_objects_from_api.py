from newsapi import NewsApiClient
import json

# key for newsAPI
newsapi_key = "8aaee90f51a245999fc29a980d1ce20c" 
newsapi = NewsApiClient(api_key=newsapi_key)

# get source ids from the merged sources and convert to comma-separated string
with open("./data/raw/merged_sources.json", "r") as file:
    sources = json.load(file)

source_str = ",".join([value["id"] for key, value in sources.items()])

# get headlines from source list
headline_objects = newsapi.get_everything(sources=source_str,
                                   language='en')

print(len(headline_objects))

with open("./data/raw/headline_objects.json", "w") as file:
    json.dump(headline_objects, file, indent=2)