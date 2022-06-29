from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
root=Tk()
root.geometry("600x600")
root.title("Color Randomization")

label1=Label(root,text="Color", bg="black", fg="white")
label1.place(relx=0.5, rely=0.1,anchor=CENTER)

class CreateElements():
    def __init__(self):
        print("Create Dynamic Elements")
    
    def NewElements(self):
        self.text=["red","orange","yellow","green","blue","purple"]
        self.color=["red","orange","yellow","green","blue","purple"]
        self.textrandom=random.randint(0,5)
        self.colorrandom=random.randint(0,5)
        self.color1=["red","orange","yellow","green","blue","purple"]
        self.colorrandom1=random.randint(0,5)
        
        label1["text"]=self.text[self.textrandom]
        label1["bg"]=self.color[self.colorrandom]
        label1["fg"]=self.color1[self.colorrandom1]

object1=CreateElements()
button2=Button(root,text="SUPRISE (If you click me)!!",command=object1.NewElements)
button2.pack()
root.mainloop()