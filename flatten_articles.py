import json

# load list of articles
with open ("./data/raw/headline_objects.json", "r") as file:
    articles = json.load(file)["articles"]

for article in articles:
    print(article["source"]["id"])


with open("./data/flattened_articles.csv", "w") as file:
    # write header row
    file.writelines("id,author,title,description,url,urlToImage,publishedAt,content\n")
    
    # write individual rows 
    for article in articles:
        row = str(article["source"]["id"]) + "," + str(article["author"]) + "," + str(article["title"]) + "," + str(article["description"]) + "," + str(article["url"]) + "," + str(article["urlToImage"]) + "," + str(article["publishedAt"]) + "," + str(article["content"]) + "\n"
        file.writelines(row)


