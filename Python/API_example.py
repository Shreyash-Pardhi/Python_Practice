import requests

res = requests.get("https://randomuser.me/api")

fname = res.json()['results'][0]['name']['first']
lname = res.json()['results'][0]['name']['last']
print(f"Name: {fname} {lname}")

gen = res.json()['results'][0]['gender']
print(f"Gender: {gen}")

email = res.json()['results'][0]['email']
print(f"Email: {email}")

dob = res.json()['results'][0]['dob']['date']
print(f"Date of Birth: {dob}")

loc = res.json()['results'][0]['location']['city']
print(f"Location: {loc}")