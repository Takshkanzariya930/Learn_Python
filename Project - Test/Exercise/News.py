import requests as r
import json
from apis import newsapi

query = input("Which type of news you want to read today : ")
n = int(input("how many news do want to read : "))
i = 1

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={newsapi}"

response = r.get(url)

news = json.loads(response.text)

for article in news["articles"]:

    if i < n + 1 :
        print(f"\n-> {article["title"]}\n")
        print(f"    {article["description"]}\n")
        print(f"    For more info '{article["url"]}'\n")
        print(f"-".center(50,"-"))
        i = i + 1
    else:
        break