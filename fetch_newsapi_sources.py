from newsapi import NewsApiClient
import json

# key for newsAPI
newsapi_key = "8aaee90f51a245999fc29a980d1ce20c" 


# This section connects to NewsAPI, GETs a list of sources, and writes it to a JSON file-----------------

newsapi = NewsApiClient(api_key=newsapi_key)

sources = newsapi.get_sources()

with open("./data/raw/newsapi_sources.json", "w") as file:
    json.dump(sources, file, indent=2)

#-------------------------------------------------------------------------------------------------------

with open("newsapi_sources.json", "r") as file:
    newsapi_sources = json.load(file)

