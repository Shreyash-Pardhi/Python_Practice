from tkinter import *
from PIL import Image,ImageTk
import requests
from io import *

root = Tk()
root.geometry("500x550")
root.title("MEME APP")

res = requests.get("https://meme-api.com/gimme")

imgurl = res.json()['url']
imgres = requests.get(imgurl)
imgdata=imgres.content
# print(imgdata)
img = ImageTk.PhotoImage(Image.open(BytesIO(imgdata)).resize(size=(450,450)))
lbl = Label(root,image=img)
lbl.place(x=20,y=0)

btn = Button(root, text='Next', font=("bold", 15), width=38)
btn.place(x=30, y=480)

root.mainloop()