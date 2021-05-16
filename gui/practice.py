from tkinter import *

window=Tk()

def kg_to_wt():
    print("Hopefully this works")
    lbs=float(e1_value.get())*2.20462
    grs=float(e1_value.get())*35.274
    ozs=float(e1_value.get())*1000
    
    
    tp.insert(END,lbs)
    tg.insert(END,grs)
    to.insert(END,ozs)

e2=Label(text="KG")
e2.grid(row=0,column=0)

b1=Button(window,text="Convert",command=kg_to_wt)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

tp=Text(window,height=1,width=15)
tp.grid(row=2,column=0)

tg=Text(window,height=1,width=15)
tg.grid(row=2,column=1)

to=Text(window,height=1,width=15)
to.grid(row=2,column=2)


window.mainloop()

