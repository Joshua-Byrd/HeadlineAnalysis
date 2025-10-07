import json
import csv

# load list of articles
with open ("./data/raw/headline_objects.json", "r") as file:
    articles = json.load(file)["articles"]

# write flattened article information to a csv
with open("./data/flattened_articles.csv", "w") as file:
    fieldnames = ["id", "name", "author", "title", "description", "url", "urlToImage", "publishedAt", "content"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    # flatten the source key in the article dict first, then write it as a row to the csv
    for article in articles:
        row_dict = {
            "id": article["source"]["id"],
            "name": article["source"]["name"],
            "author": article["author"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "urlToImage": article["urlToImage"],
            "publishedAt": article["publishedAt"],
            "content": article["content"]
        }
        writer.writerow(row_dict)

