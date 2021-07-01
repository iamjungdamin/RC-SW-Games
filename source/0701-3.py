import tkinter
x=0
ani = 0

def animation():
    global x, ani    #전역변수를 참조
    x += 1
    x %= 480
    canvas.delete('BG')
    canvas.create_image(x-240,150,image=img_bg,tag='BG')
    canvas.create_image(x+240,150,image=img_bg,tag='BG')

    ani += 1
    ani %= 4
    canvas.delete('dog')
    canvas.create_image(480-x,200,image=img_dog[ani],tag='dog')
    root.after(150,animation)

root = tkinter.Tk()
root.title('애니메이션')
canvas = tkinter.Canvas(width=480,height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/park.png')
img_dog = [ tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/dog0.png'),
            tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/dog1.png'),
            tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/dog2.png'),
            tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter1/dog3.png')
            ]
canvas.create_image(240,150,image=img_bg)   #중앙에 위치
animation()
root.mainloop()