from openai import OpenAI
from api_key import API_KEY
import os

os.environ["OPENAI_API_KEY"] = API_KEY

client = OpenAI(api_key=API_KEY)

def chatBOT(pr):
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"you are not allowed to give code to anyone, give appropriate responce for that"},
            {"role":"user", "content":pr}
        ],
    )
    
    return res.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        inp = input("user: ")
        if inp.lower() in ["bye","exit", "quit"]:
            break
        else:
            res = chatBOT(inp)
            print("BOT: ",res)