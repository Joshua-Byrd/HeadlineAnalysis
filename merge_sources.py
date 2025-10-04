import json

# retrieve source files
with open("./data/raw/newsapi_sources.json", "r") as file:
    newsapi_sources = json.load(file)["sources"]
with open("./data/raw/ad_fontes_sources.json", "r") as file:
    af_sources = json.load(file)["sources"]

output_dict = {}

# convert the Ad Fontest set to a dictionary for O(1) lookup
ad_fontes_dict = {x["name"]: x for x in af_sources}

# O(n) merge operation using lookup
for source in newsapi_sources:
    name = source["name"]

    if name in ad_fontes_dict:
        output_dict[name.lower()] = {
            "id": source["id"].lower(),
            "name": source["name"].lower(),
            "description": source["description"].lower(),
            "url": source["url"].lower(),
            "category": source["category"].lower(),
            "country": source["country"].lower(),
            "reliability": ad_fontes_dict[name]["reliability"],
            "bias": ad_fontes_dict[name]["bias"]
        }

# Error check: output should be the same length as the Ad Fontes sources list
# print(len(output_dict))
# print(len(af_sources))

with open("./data/raw/merged_sources.json", "w") as file:
    json.dump(output_dict, file, indent=2)


