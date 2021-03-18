from tkinter import *
HEIGHT = 750
WIDTH = 250

class App(Frame):
    def __init__(self,master):
        pass

    def create_widgits(self):
        pass



def main():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    app = App(root)
    root.mainloop()

main()
