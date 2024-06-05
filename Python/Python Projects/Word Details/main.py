import requests
word = input("Enter a word: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
pos = ["noun","verb","adverb","preposition","adjective","pronoun","interjection","conjunction"]
res = requests.get(url)
flag = False
# print(f"{res.json()['message']}\n{res.json()['resolution']}")

for i in range(len(pos)):
    for j in range(len(pos)):
        try:
            if res.json()[j]['meanings'][i]['partOfSpeech'] in pos:
                print("\n----------------------- POS:",res.json()[j]['meanings'][i]['partOfSpeech'],"-----------------------")
                print("Definition: ",res.json()[j]['meanings'][i]['definitions'][0]['definition'])
                try:
                    exm = res.json()[j]['meanings'][i]['definitions'][0]['example']
                except Exception as e:
                    exm = "__"
                print("Example: ",exm)
                print("Synonyms: ",res.json()[j]['meanings'][i]['synonyms'])
                print("Antonyms: ",res.json()[j]['meanings'][i]['antonyms'])
                flag = True
                continue
                
        except Exception as e:
            continue

if(flag == False):
    print(f"{res.json()['message']}\n{res.json()['resolution']}")