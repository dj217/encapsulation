from tkinter import *
import random

root=Tk()
root.title("encapsulation")
root.geometry("500x400")
root.config(bg="white")

cn=Label(root,text="Score:0",font=("Ariel",40),bg="white")
cn.place(relx=0.1,rely=0.1,anchor=CENTER)

cnl=Label(root,font=("Ariel",40),bg="white")
cnl.place(relx=0.5,rely=0.3,anchor=CENTER)

cne=Entry(root)
cne.place(relx=0.5,rely=0.5,anchor=CENTER)

class g:
    def __init__(self):
        self.__score=0
    def up(self):
        self.text=["BLACK","PINK","YELLOW","ORANGE","RED"]
        self.random=random.randint(0,5)
        self.color=["black","pink","yellow","orange","red"]
        self.r=random.randint(0,5)
        cnl["text"]=self.text[self.random]
        cnl["fg"]=self.text[self.r]
        
    def us(self,iv):
        if(iv==self.color[self.random]):
            print(self.color[self.random])
            self.__score=self.__score+random.randint(0,10)
            cnl["text"]="score :"+str(self.__score)
    def gsv(self,iv):
        self.__us(iv)
obj=g()

def getinput():
    value=iv.get()
    obj.gsv(value)
    obj.up()
    iv.delete(0,END)
    
btn = Button(root, text="CHECK" ,command=getinput, bg="dark olive green", fg="black", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.35,rely=0.65,anchor=CENTER)
btn = Button(root, text="START" ,command=obj.up, bg="dark olive green", fg="black", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.65,rely=0.65,anchor=CENTER)
root.mainloop()