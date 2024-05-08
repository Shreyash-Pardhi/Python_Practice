# Using String Indexes
# def pallindrome(string):
#     if(string == string[::-1]):
#         return 'Palindrome'
#     else:
#         return 'Not a Pallindrome'

# string = input()
# print(pallindrome(string))

#Using normal logic
string = input()
def pallindrome(str):
    flag=0
    l=0
    r=len(string)-1
    for i in range (len(string)):
        if(l==r and string[l]==string[r]):
            flag = 1
        else:
            if(string[l]==string[r]):
                l+=1
                r-=1
                if(l==r and string[l]==string[r]):
                    flag = 1
    if(flag==1):
        return 'Pallindrome'
    else:
        return 'Not a Pallindrome'

print(pallindrome(string))