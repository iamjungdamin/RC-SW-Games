from tkinter import *
window = Tk()

def process():
    dollar = float(e1.get())
    e2.insert(0,str(dollar*1127))

l1 = Label(window, text='달러',font='helvetica 16 italic')
l2 = Label(window, text='원',font='helvetica 16 italic')
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1 = Entry(window,bg='yellow',fg='black')
e2 = Entry(window,background='blue',foreground='white')
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window, text='달러->원',command=process)
b2 = Button(window, text='원->달러')
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b1.configure(font='helvetica 12')
b2['bg'] = 'green'

#L1 = Label(window, text='김영식', bg='red', fg='white', font='helvetica 16 italic')
#L2 = Label(window, text='정다민', bg='green', fg='white')
#L1.place(x=0,y=0)
#L2.place(x=100,y=30)
window.mainloop()

