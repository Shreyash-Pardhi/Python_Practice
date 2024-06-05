from openai import OpenAI
from api_key import API_KEY
import os

os.environ["OPENAI_API_KEY"] = API_KEY

cli = OpenAI()

out = cli.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are expert in Machine Learning."},
        {"role": "user", "content": "Explain how does random forest works?."}
    ]
)

print(out.choices[0].message)