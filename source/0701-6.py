import tkinter
import math

def hit_check_rect():
    dis = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )   # **2는 ^2
    # dis = ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5   # 이렇게도 가능
    if dis <= r1+r2:
        return True
    return False

def mouse_move(e):
    global x1, y1
    x1 = e.x
    y1 = e.y
    color = 'green'
    if hit_check_rect() == True:
        color = 'lime'
    canvas.delete('CIR1')
    canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill=color,tag='CIR1')

root = tkinter.Tk()
root.title('원을 사용한 히트 체크')
canvas = tkinter.Canvas(width=600,height=400,bg='white')
canvas.pack()
canvas.bind('<Motion>',mouse_move)

x1,y1,r1 = 50,50,40
x2,y2,r2 = 300,200,80

canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill='green',tag='CIR1')
canvas.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill='yellow')
root.mainloop()