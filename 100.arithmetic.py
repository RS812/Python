from tkinter import*
def addition():
    v1=int(txt1.get())
    v2=int(txt2.get())
    ans=v1+v2
    lblans.config(text=f"Your answer is:{ans}")
def substraction():
    v1=int(txt1.get())
    v2=int(txt2.get())
    ans=v1-v2
    lblans.config(text=f"Your answer is:{ans}")
def multiplication():
    pass
def division():
    pass
scr=Tk()
scr.title("Arithmetic Operations")
scr.geometry("300x200")
txt1=Entry(scr)
txt2=Entry(scr)
lblans=Label(scr,text="Your answer is :")
btnAdd=Button(master=scr,text="Addition",command=addition)
btnSub=Button(master=scr,text="Substraction",command=substraction)
btnMul=Button(master=scr,text="Multiplication",command=multiplication)
btnDiv=Button(master=scr,text="Division",command=division)
txt1.pack()
txt2.pack()
btnAdd.pack()
btnSub.pack()
btnMul.pack()
btnDiv.pack()
lblans.pack()
scr.mainloop()

