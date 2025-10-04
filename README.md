# Sentiment Analysis of News Headlines

## Steps taken so far
1. Connected to NewsAPI and downloaded list of sources, which were then written to ./data/raw/newsapi_sources.json (fetch_newsapi_sources.py)
2. Manually created a JSON object of news sources from Ad Fontes based on the sources from NewsAPI in ./data/raw/as_dontes_sources.json.  There is not a 1-to-1 correlation between the two lists of sources as not everything from NewsAPI was available from Ad Fontes.
3. Merged the list of sources into one written ./data/raw to merged_sources.json(merge_sources.py). 
4. Ran script (once) to get a list of headlines objects from NewsAPI (fetch_hl_objects_from_api.py). saved to ./data/raw/headline_objects.json.
