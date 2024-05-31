with open("Assignments\\Test Input Analysis\\text.txt") as file:
    text = "".join(file.readlines())

Total_Characters = len(text)
Total_Words = len(text.split())
Total_Sentences = len([i for i in text.split() if i.endswith('.')])
print(f"\nTotal Characters: {Total_Characters}")
print(f"Total Words: {Total_Words}")
print(f"Total Sentences: {Total_Sentences}")
print("The most common words with frequency: ", end="")
max = 0
for i in text.split():
    if (text.split()).count(i) > max:
        max = (text.split()).count(i)

for i in set(text.split()):
    if (text.split()).count(i) == max:
        print(f"{i}:{max}", end=",  ")