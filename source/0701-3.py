import tkinter

root = tkinter.Tk()
root.title('Canvas에 화면 그리기')
canvas = tkinter.Canvas(width=480,height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/park.png')
canvas.create_image(240,150,image=img_bg)   #중앙에 위치
root.mainloop()