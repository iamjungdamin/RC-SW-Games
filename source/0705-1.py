import tkinter

key = ''
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    # global koff
    # koff = True
    global key
    key = ''

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0,1,0,2]
tmr = 0
score = 0

pen_x = 90
pen_y = 90
pen_d = 0   #펜펜의 방향 변수
pen_a = 0   #펜펜의 이미지 번호

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

def draw_txt(txt,x,y,siz,col):
    fnt = ('Times New Roman', siz, 'bold')
    canvas.create_text(x+2,y+2,text=txt,fill='black',font=fnt,tag='SCREEN') #문자열 그림자
    canvas.create_text(x,y,text=txt,fill=col,font=fnt,tag='SCREEN') #문자열

def draw_screen():
    canvas.delete('SCREEN')
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]], tag='SCREEN')
    canvas.create_image(pen_x,pen_y,image=img_pen[pen_a],tag='SCREEN')
    draw_txt('SCORE '+str(score),180,30,30,'white')

def check_wall(cx,cy,dir,dot):
    #dot은 한번에 움직이는 픽셀 크기
    chk = False

    if dir == DIR_UP:
        #픽셀 좌표를 맵데이터 좌표로 변환
        #좌상,우상
        mx = (cx-30) // 60
        my = (cy-30-dot) // 60
        if map_data[my][mx] <= 1:   #맵데이터 0,1은 벽
            chk = True
        mx = (cx+29) // 60
        if map_data[my][mx] <= 1:
            chk = True

    if dir == DIR_DOWN:
        #좌하,우하
        mx = (cx-30) // 60
        my = (cy+29+dot) // 60
        if map_data[my][mx] <= 1:
            chk = True
        mx = (cx+29) // 60
        if map_data[my][mx] <= 1:
            chk = True

    if dir == DIR_LEFT:
        #좌상,좌하
        mx = (cx-30-dot) // 60
        my = (cy-30) // 60
        if map_data[my][mx] <= 1:
            chk = True
        my = (cy+29) // 60
        if map_data[my][mx] <= 1:
            chk = True

    if dir == DIR_RIGHT:
        #우상,우하
        mx = (cx+29+dot) // 60
        my = (cy-30) // 60
        if map_data[my][mx] <= 1:
            chk = True
        my = (cy+29) // 60
        if map_data[my][mx] <= 1:
            chk = True

    return chk

def move_penpen():
    global pen_x, pen_y, pen_d, pen_a, score
    if key == 'Up':
        pen_d = DIR_UP
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_y -= 20
    if key == 'Down':
        pen_d = DIR_DOWN
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_y += 20
    if key == 'Left':
        pen_d = DIR_LEFT
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_x -= 20
    if key == 'Right':
        pen_d = DIR_RIGHT
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_x += 20
    pen_a = pen_d*3 + ANIMATION[tmr%4]  #0,1,2,3 -> 0,3,6,9(방향) -> 0,1,0,2(인덱스)만큼 더해줌
    mx = pen_x // 60
    my = pen_y // 60
    if map_data[my][mx] == 3:   #사탕먹으면
        score += 100
        map_data[my][mx] = 2    #바닥으로

def main():
    global key, koff, tmr
    tmr += 1
    draw_screen()
    move_penpen()
    # if koff == True:
    #     key = ''
    #     koff = False
    root.after(100,main)

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
img_pen = [
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen00.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen01.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen02.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen03.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen04.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen05.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen06.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen07.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen08.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen09.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen10.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/pen11.png')
]
root.bind('<Key>',key_down)
root.bind('<KeyRelease>',key_up)
main()
root.mainloop()