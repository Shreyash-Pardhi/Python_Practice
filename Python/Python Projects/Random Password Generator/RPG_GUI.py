from tkinter import *
from tkinter import ttk
import string
import random
root = Tk()
root.geometry("325x400")
root.minsize(325,400)
root.maxsize(325,400)
root.title("Random Password Generator")
root.configure(bg="#80BCBD")
root.iconbitmap("Python Projects\\Random Password Generator\\password_icon.ico")

def pr():
    li.delete(0,END)
    specialChar = '@_!#$%^&*()<>?/|}{~:]'
    passwordFormat = string.ascii_letters+specialChar+string.digits if (sym.get())=='YES' else string.ascii_letters+string.digits
    for i in range(1,(int(ch.get())+1)):
        gen = "".join(random.choices(passwordFormat, k=int(n.get())))
        li.insert(END, f"{i})  {gen}")

Label(root, text="Enter Length: ",font=("bold",15),bg="#80BCBD").place(x=10,y=20)
n = Spinbox(root, font=("bold",10),from_=5, to=30, width=8,bg="#AAD9BB")
n.place(x=170,y=25)

Label(root, text="Include Symbols: ",font=("bold",15),bg="#80BCBD").place(x=10,y=60)
sym = ttk.Combobox(root,values=["YES","NO"],width=8,state="readonly",background='red')
sym.place(x=170, y=65)
sym.current(0)

Label(root, text="No. of Choices: ",font=("bold",15),bg="#80BCBD").place(x=10,y=100)
ch = Spinbox(root, font=("bold",10),from_=1, to=30, width=8,bg="#AAD9BB")
ch.place(x=170,y=105)

# scr = Scrollbar(root, orient='vertical')
# scr.place(x=200,y=152)

b = Button(root, text="Generate", font=("bold",15),bg="#92C7CF",width=20,command=pr)
b.place(x=45,y=140)

li = Listbox(root,font=(100),width=33,bg="#EAECCC")
li.place(x=10,y=190)

root.mainloop()
