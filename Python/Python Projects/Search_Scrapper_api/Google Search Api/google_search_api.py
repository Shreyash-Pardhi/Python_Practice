import sys
sys.path.insert(0,"D:\\Work and Assignments\\Python\\Python Projects\\Search_Scrapper_api")

import requests
from api_key import API_KEY

prompt = "chat"#input("Enter to search: ")
url = "https://www.searchapi.io/api/v1/search"
params = {
    "api_key": API_KEY,
    "engine": "google",
    "q": prompt
}

categories = [
"knowledge_graph",
"organic_results",
"related_questions",
"inline_videos",
"related_searches"
]
res = requests.get(url, params = params)


for key1 in categories:
    try:
        for i in res.json()[key1]:
           print(i)
    except Exception as e:
        print("here: ",e)
        continue
