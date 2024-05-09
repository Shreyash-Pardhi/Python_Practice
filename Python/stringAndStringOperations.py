s1 = 'shreYasH' #string in single quotes
s2 = "'shreyash' is" #string in double quotes
s3 = '''"'shreyash' is" a''' #string in tripple quotes
print(s1)
print(s2)
print(s3)

#String operations
#1)indexes
print('string first letter:',s1[0])
print(s1[0:3])
print(s1[1:])
print(s1[:5])
print(s1[::2]) #s1[start:end:gap with order]
print(s1[::]) #takes default values

#2)methods
print(s1.upper()) #capitalize all letters in a string
print(s1.lower()) #prints all letters in lower case
print(s1.find('s')) #returns 1st position of the entered string or character
print(s1.capitalize()) #capitalizes 1st letter of string
print('abc'.center(20,'~')) #center allign
print('def'.ljust(20,'#')) #left allign
print('ghi'.rjust(30,'+')) #right allign
print(s1.strip())