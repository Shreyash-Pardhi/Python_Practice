from tkinter import *
import NGG

root = Tk()
root.geometry("400x300")
root.title("Number Guessing Game")

Label(root,text="Number Guessing Game",font=("bold",20)).place(x=50,y=15)  
Label(root, text="Enter the range to choose from..",font=(15)).place(x=15,y=70) 

Label(root,text="From: ",font=(10)).place(x=15,y=100) 
From = Entry(root)
From.place(x=70,y=103)

Label(root,text="To: ",font=(10)).place(x=15,y=125)
To = Entry(root)
To.place(x=70,y=128)

Label(root,text="Attempts: ",font=(10)).place(x=15,y=155)
Label(root,text="0",font=(10)).place(x=85,y=156)

Label(root,text="Guess no.: ",font=(10)).place(x=15,y=181)
Guss = Entry(root,width=15)
Guss.place(x=100,y=184)

Label(root,text=".....Result.....",font=(10),state="disabled",width=19,height=5,bg="#dbd7d2").place(x=210,y=100) 

button = Button(text="Guess",font=(15),width=30,bg="#555555",command=NGG.Operations).place(x=55,y=225)


root.mainloop()