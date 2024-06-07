import sys
sys.path.insert(0,"D:\\Work and Assignments\\Python\\Python Projects\\Search_Scrapper_api")

from api_key import API_KEY
import requests

prompt = input("Enter Product name: ")
url = "https://www.searchapi.io/api/v1/search"
params = {
    "api_key": API_KEY,
    "engine": "amazon_search",
    "q": prompt
}
# _ = "___"
res = requests.get(url=url, params=params)
for i in range(len(res.json()['organic_results'])):
    try:
        print(f"\n{i+1}) Product : {res.json()['organic_results'][i]['title']}")
        print(f"    Rating : {res.json()['organic_results'][i]['rating']}")
        print(f"    Reviews : {res.json()['organic_results'][i]['reviews']}")
        # print(f"    Original Price : {res.json()['organic_results'][i]['original_price'] if not Exception else _}")
        print(f"    Best Price : {(res.json()['organic_results'][i]['extracted_price'])*83.50}")
        print(f"    Stock : {res.json()['organic_results'][i]['availability']}")
    except Exception as e:
        continue
    
    
    