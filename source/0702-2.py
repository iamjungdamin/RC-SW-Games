import tkinter
import math

root = tkinter.Tk()
root.title('삼각함수를 활용한 도형 그리기')
canvas = tkinter.Canvas(width=600,height=600,bg='black')
canvas.pack()

COLOR= ['greenyellow','limegreen', 'aquamarine', 'cyan', 'deepskyblue',
        'blue', 'blueviolet', 'violet']

for d in range(360):
    a=math.radians(d)
    x = 250*math.cos(a)
    y = 250*math.sin(a)
    canvas.create_line(300,300,300+x,300+y,fill=COLOR[d%8],width=2)
    
root.mainloop()