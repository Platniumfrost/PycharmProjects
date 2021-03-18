from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 800
WIDTH = 250
index = 0

class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.pack(fill = BOTH,expand=1)
        self.index = 0
        self.create_widgits()

    def create_widgits(self):
        self.config(bg="DarkGrey")
        Label(text="my favorite Images",width=20).place(x=(WIDTH/2)-70,y=5)
        #loaded images
        img1 = Image.open("dead_cells.png")
        img2 = Image.open("Muramasa.jpg")
        img3 = Image.open("Nargacuga.jpg")
        # convert img to tk objects
        logo1 = ImageTk.PhotoImage(img1)
        logo2 = ImageTk.PhotoImage(img2)
        logo3 = ImageTk.PhotoImage(img3)
        self.imglist = [logo1,logo2,logo3]

        self.imglbl1 = Label(self,image=self.imglist[0])
        self.imglbl1.image = self.imglist[0]
        self.imglbl1.place(x=25,y=65)
        imglbl2 = Label(self,image=self.imglist[1])
        imglbl2.image = self.imglist[1]
        imglbl2.place(x=25,y=295)
        imglbl3 = Label(self,image=self.imglist[2])
        imglbl3.image = self.imglist[2]
        imglbl3.place(x=25,y=490)


        bttn1= Button(self, text="Switch to img 1")
        bttn1.place(x=0,y=750)
        bttn2 = Button(self, text="Switch to img 2")
        bttn2.place(x=0,y=775)
        bttn3 = Button(self, text="Switch to img 3")
        bttn3.place(x=93,y=760)

        change = Button(text = "change img" , command = self.changeimg)
        change.place(x=25 , y=650)

    def changeimg(self):
        if self.index > len(self.imglist)-1:
            self.index = 0
        self.index +=1
        self.imglbl1.config(image=self.imglist[self.index])



def main():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    app = App(root)
    root.mainloop()

main()
