import tkinter

key = ''
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

pen_x = 90
pen_y = 90

map_data = [
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
    [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
    [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
    [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
    [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]   #9행 12열

def draw_screen():
    canvas.delete('SCREEN')
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]], tag='SCREEN')
    canvas.create_image(pen_x,pen_y,image=img_pen,tag='SCREEN')

def check_wall(cx,cy,dir):
    chk = False

    if dir == DIR_UP:
        #픽셀 좌표를 맵데이터 좌표로 변환
        mx = cx // 60
        my = (cy-60) // 60

    if dir == DIR_DOWN:
        mx = cx // 60
        my = (cy+60) // 60

    if dir == DIR_LEFT:
        mx = (cx-60) // 60
        my = cy // 60

    if dir == DIR_RIGHT:
        mx = (cx+60) // 60
        my = cy // 60
    
    if map_data[my][mx] <= 1:   #맵데이터 0,1은 벽
        chk = True
    return chk

def move_penpen():
    global pen_x, pen_y
    if key == 'Up':
        if check_wall(pen_x,pen_y,DIR_UP) == False:
            pen_y -= 60
    if key == 'Down':
        if check_wall(pen_x,pen_y,DIR_DOWN) == False:
            pen_y += 60
    if key == 'Left':
        if check_wall(pen_x,pen_y,DIR_LEFT) == False:
            pen_x -= 60
    if key == 'Right':
        if check_wall(pen_x,pen_y,DIR_RIGHT) == False:
            pen_x += 60

def main():
    global key, koff
    draw_screen()
    move_penpen()
    if koff == True:
        key = ''
        koff = False
    root.after(300,main)

root = tkinter.Tk()
root.title('아슬아슬 펭귄 미로')
root.resizable(False,False)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()

img_bg = [
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/chip00.png'),    #벽
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/chip01.png'),    #벽
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/chip02.png'),    #바닥
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/chip03.png')     #캔디
]
img_pen = tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen03.png')
root.bind('<Key>',key_down)
root.bind('<KeyRelease>',key_up)
main()
root.mainloop()