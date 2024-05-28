from tkinter import *
from PIL import Image,ImageTk
import requests
from io import *

class MEME:
    def __init__(self, root, api):
        self.root = root
        self.api = api
        self.imgLabel = Label(root,relief='solid')
        self.imgLabel.place(x=20,y=10)
        self.nextButton = Button(root, text='Next', font=("bold", 15),fg="#FFF6E0", bg="#61677A",relief='groove', activebackground="#252B48",activeforeground="#FFF6E0",width=38,command=self.nextIMG)
        
        self.nextButton.place(x=30, y=490)
        self.nextIMG()
    
    def fetchURL(self):
        try:
            res = requests.get(self.api)
            return(res.json()['url'])
        except Exception as e:
            print("Failed to fetch Image Url",e)
    
    def fetchIMG(self,url):
        res = requests.get(url)
        res.raise_for_status()
        return Image.open(BytesIO(res.content))
    
    def nextIMG(self):
        imgURL = self.fetchURL()
        img = self.fetchIMG(imgURL)
        self.displayIMG(img)
 
    def displayIMG(self, img):
        tk_image = ImageTk.PhotoImage(img.resize(size=(450,450)))
        self.imgLabel.config(image=tk_image)
        self.imgLabel.image = tk_image
 
if __name__ == "__main__":
    root = Tk()
    root.geometry("500x550")
    root.minsize(500,550)
    root.maxsize(500,550)
    root.configure(bg="#272829")
    root.title("MEME APP")
    meme = MEME(root,"https://meme-api.com/gimme")
    root.mainloop()