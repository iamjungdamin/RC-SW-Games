from tkinter import *
window = Tk()

def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image = img)
    imageLabel.image = img
    
photo = PhotoImage(file='RC-SW-Games/source/image/우주소녀.gif')

imageLabel = Label(window, image=photo)
imageLabel.pack()
inputBox = Entry(window)
inputBox.pack()

Button(window,text='클릭',command=change_img).pack()
window.mainloop()