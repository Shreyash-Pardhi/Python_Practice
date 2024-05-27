from tkinter import *
import random

root = Tk()
root.geometry("400x300")
root.maxsize(400,300)
root.minsize(400,300)
root.title("Number Guessing Game")
root.configure(bg="#40A578")
img = PhotoImage(file="Python Projects\\Number Guessing Game\\numberguessing1.png")
root.iconphoto(False, img)

num =0
totalAttempts =0

def ffrroomm(*args):
    global totalAttempts
    global num
    v1 = int(e1.get())
    v2 = int(e2.get())
    sm = (v1 + v2).bit_length()-1
    totalAttempts = sm
    num = random.randint(v1, v2)
    lbl.set(sm)
    
def Operations():
    try: 
        global num
        global totalAttempts
        lbl.set(totalAttempts-1)
        guess = int(Guess.get())
        if(num == 0):
            lbl.set(0)
            result["text"]="Please enter\nthe range first"
            return
        if(guess>num):
            result["text"]="Guessed number is\ntoo high"
            totalAttempts-=1
        elif(guess<num):
            result["text"]= "Guessed number is\ntoo low"
            totalAttempts-=1
        else:
            result["text"]= "Congratulations\nYou guessed it!!"
            e1.set('')
            e2.set('')
            num = None
            return
        if(totalAttempts==0):
            result["text"]= "Nice Try\nBetter luck next time..."
            e1.set('')
            e2.set('')
            num = None
            return
    except Exception as e:
        result["text"] = "Please\nproperly enter the range\nand number to guess"
        lbl.set(0)


Label(root,text="Number Guessing Game",font=("bold",20),bg="#40A578").place(x=50,y=15)  
Label(root, text="Enter the range to choose from..",font=(15),bg="#40A578").place(x=15,y=70) 

e1 = StringVar()
e2 = StringVar()
e1.trace_add("write", ffrroomm)
e2.trace_add("write", ffrroomm)

Label(root,text="From: ",font=(10),bg="#40A578").place(x=15,y=100) 
From = Entry(root,textvariable=e1,bg="#9DDE8B")
From.place(x=70,y=103)

Label(root,text="To: ",font=(10),bg="#40A578").place(x=15,y=125)
To = Entry(root, textvariable=e2,bg="#9DDE8B")
To.place(x=70,y=128)

lbl = StringVar()
lbl.set('0')
Label(root,text="Attempts: ",font=(10),bg="#40A578").place(x=15,y=155)
attrmpt = Label(root,font=(10),textvariable=lbl,bg="#40A578")
attrmpt.place(x=85,y=156)

Label(root,text="Guess no.: ",font=(10),bg="#40A578").place(x=15,y=181)
Guess = Entry(root,width=15,bg="#9DDE8B")
Guess.place(x=100,y=184)

result = Label(root,text="",font=(10),width=19,height=5,bg="#E6FF94")
result.place(x=210,y=100)

button = Button(text="Guess",font=("bold",15),width=30,bg="#006769",command=Operations).place(x=30,y=225)


root.mainloop()