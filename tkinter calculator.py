
from tkinter import *
win=Tk()
win.geometry("400x600")
win.title("calculator")  
win.iconbitmap("vector-calculator-icon.ico")
def func1():
    ent.delete(0,END)
    
def func2():
    x = var.get()
    y = eval(x) 
    var.set(y)
def fdelt():
       ent.delete(len(ent.get())-1,END) 

def fdiv():
       x=var.get()
       var.set(x+"/")
    
def fone():
    x = var.get()
    var.set(x + '1')

def ftwo():
    x = var.get()
    var.set(x + '2')
def fthree():
       x=var.get()
       var.set(x+"3")
def fmult():
       x=var.get()
       var.set(x+"*")
def ffour():
       x=var.get()
       var.set(x+"4")
def ffive():
       x=var.get()
       var.set(x+"5")
def fsix():
       x=var.get()
       var.set(x+"6")
def fminus():
       x=var.get()
       var.set(x+"-")
def fseven():
       x=var.get()
       var.set(x+"7")
def feight():
       x=var.get()
       var.set(x+"8")
def fnine():
       x=var.get()
       var.set(x+"9")
def fplus():
       x=var.get()
       var.set(x+"+") 
def fzero():
       x=var.get()
       var.set(x+"0") 
def  fdot():
      x=var.get()
      var.set(x+".")    


var=StringVar()

ent=Entry(win,font=('arial',15,'bold'),textvariable=var,highlightbackground="black")
ent.place(x=0,y=0,height=50,width=300)
delt=Button(win,text="x",command=fdelt)
delt.place(x=300,y=0,height=50,width=100)
clr=Button(win,text="C",command=func1)
clr.place(x=0,y=50,height=50,width=300)
div=Button(win,text="/",command=fdiv)
div.place(x=300,y=50,height=50,width=100)
one=Button(win,text="1",command=fone)
one.place(x=0,y=100,height=50,width=100)
two=Button(win,text="2",command=ftwo)
two.place(x=100,y=100,height=50,width=100)
three=Button(win,text="3",command=fthree)
three.place(x=200,y=100,height=50,width=100)
mult=Button(win,text="*",command=fmult)
mult.place(x=300,y=100,height=50,width=100)
four=Button(win,text="4",command=ffour)
four.place(x=0,y=150,height=50,width=100)
five=Button(win,text="5",command=ffive)
five.place(x=100,y=150,height=50,width=100)
six=Button(win,text="6",command=fsix)
six.place(x=200,y=150,height=50,width=100)
minus=Button(win,text="-",command=fminus)
minus.place(x=300,y=150,height=50,width=100)
seven=Button(win,text="7",command=fseven)
seven.place(x=0,y=200,height=50,width=100)
eight=Button(win,text="8",command=feight)
eight.place(x=100,y=200,height=50,width=100)
nine=Button(win,text="9",command=fnine)
nine.place(x=200,y=200,height=50,width=100)
plus=Button(win,text="+",command=fplus)
plus.place(x=300,y=200,height=50,width=100)
zero=Button(win,text="0",command=fzero)
zero.place(x=0,y=250,height=50,width=200)
dot=Button(win,text=".",command=fdot)
dot.place(x=200,y=250,height=50,width=100)
equal=Button(win,text="=",command=func2)
equal.place(x=300,y=250,height=50,width=100)
win.mainloop() 
