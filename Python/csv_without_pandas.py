import csv
data = []
with open("D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\results.csv", 'r') as file:
    csvfile = csv.reader(file)
    
    for row in csvfile:
        data.append(row)

print(data[3][2])