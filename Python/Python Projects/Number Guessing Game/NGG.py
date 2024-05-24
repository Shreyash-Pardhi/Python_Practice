import random

if __name__ == '__main__':
    print("Number Guessing Game\nEnter the range...")
    From = int(input("from :"))
    To = int(input("to :"))
    num = random.randint(From, To)
    totalAttempts =(From + To).bit_length()
    
    if (From and To)!=None:
        while(totalAttempts>0):
            print(f"\nYou have {totalAttempts} attempts")
            guess = int(input("Guess the number :"))
            if(guess>num):
                print("Guess is high")
                totalAttempts-=1
            elif(guess<num):
                print("Guess is low")
                totalAttempts-=1
            else:
                print("Congratulations, You guessed it!!")
                break
    if(totalAttempts==0):
        print("\nNice Try, Better luck next time...")