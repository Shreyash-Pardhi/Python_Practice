import re
str = "123@delaplex.com 12 12 131"
g = re.search("@delaplex.com$", str)
print(f'Valid Delaplex Employee' if g else 'Not a delaplex Employee')

a = re.findall("1\Z", str)
#print(" ".join(a))
print(a)

mob='000008788904106'
_mob=mob.lstrip('0')
b = re.findall("^[1-9].{8}[0-9]$", _mob)
print(f"{b},Valid mobile number" if b else "Not a Valid number! Check again")

msg = "the regex part is little difficult but interesting"
c = re.split("\s", msg, 3)
print(c)

