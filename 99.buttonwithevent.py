from tkinter import *
def welcomemsg(event):
    print("You just Clicked me....")
scr=Tk()
scr.title("Button Example !!!!")
scr.geometry("300x200")
btn1=Button(master=scr,text="Click me....")
btn1.pack()
btn1.bind("<Button>",welcomemsg)
def welcome():
    print("You Clicked me...")
btn2=Button(master=scr,text="Click me....",command=welcome)
btn2.pack()
scr.mainloop()
