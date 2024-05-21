import random
import string

if __name__ == "__main__":
    n = int(input("Enter Length of the Password: "))
    isSpecial = input("Do you want to include Special Symbols (y/n): ")
    howMany = int(input("How many options do you want: "))
    
    specialChar = '@_!#$%^&*()<>?/|}{~:]'
    passwordFormat = string.ascii_letters+specialChar+string.digits if isSpecial=='y' else string.ascii_letters+string.digits
    
    for i in range(1,(howMany+1)):
        gen = "".join(random.choices(passwordFormat, k=n))
        print(f"{i}) {gen}")