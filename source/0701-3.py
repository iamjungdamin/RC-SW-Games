import tkinter
x=0

def scroll_bg():
    global x    #전역변수를 참조
    x += 1
    x %= 480
    canvas.delete('BG')
    canvas.create_image(x-240,150,image=img_bg,tag='BG')
    canvas.create_image(x+240,150,image=img_bg,tag='BG')
    root.after(50,scroll_bg)

root = tkinter.Tk()
root.title('Canvas에 화면 그리기')
canvas = tkinter.Canvas(width=480,height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/park.png')
canvas.create_image(240,150,image=img_bg)   #중앙에 위치
scroll_bg()
root.mainloop()