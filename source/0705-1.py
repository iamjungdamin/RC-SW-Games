import tkinter
import random

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

idx = 0     # 0 타이틀, 1 게임중, 2 게임오버, 3 클리어
tmr = 0
stage = 1
score = 0
candy = 0

pen_x = 0
pen_y = 0
pen_d = 0   #펜펜의 방향 변수
pen_a = 0   #펜펜의 이미지 번호

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0
red_sy = 0

map_data = []

def set_stage():
    global map_data, candy
    global red_sx, red_sy

    if stage == 1:
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
        candy = 32
        red_sx = 630
        red_sy = 450

    if stage == 2:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 3, 0],
            [0, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 0],
            [0, 2, 1, 3, 3, 3, 3, 3, 3, 1, 2, 0],
            [0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 0],
            [0, 3, 3, 1, 2, 1, 1, 2, 1, 3, 3, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90

    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 0, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450

def set_char_pos():
    global pen_x,pen_y,pen_d,pen_a
    global red_x,red_y,red_d,red_a
    global red_sx, red_sy
    pen_x, pen_y = 90, 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x, red_y = red_sx, red_sy
    red_d = DIR_DOWN
    red_a = 3

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
    canvas.create_image(red_x,red_y,image=img_red[red_a],tag='SCREEN')
    draw_txt('SCORE '+str(score),180,30,30,'white')
    draw_txt('STAGE '+str(stage),520,30,30,'lime')

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
    global pen_x, pen_y, pen_d, pen_a, score, candy
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
        candy -= 1

def move_enemy():
    global idx, tmr
    global red_x, red_y, red_d, red_a
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:
        red_d = random.randint(0,6)
        if red_d >= 4:  #펜펜을 따라간다
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d < DIR_RIGHT

    if red_d == DIR_UP:
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_y -= speed
    if red_d == DIR_DOWN:
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_y += speed
    if red_d == DIR_LEFT:
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_x -= speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_x += speed
    red_a = red_d*3 + ANIMATION[tmr%4]

    if abs(red_x-pen_x) <= 40 and abs(red_y-pen_y) <= 40:
        idx = 2     #게임종료
        tmr = 0

def main():
    global key, koff, idx, tmr, stage, score
    tmr += 1
    draw_screen()
    
    if idx == 0:
        canvas.create_image(360,200,image=img_title,tag='SCREEN')
        if tmr%10 < 5:
            draw_txt('Press Space !!', 360, 380, 30, 'yellow')
        if key == 'space':
            stage = 1
            score = 0
            set_stage()
            set_char_pos()
            idx = 1

    if idx == 1:
        move_penpen()
        move_enemy()
        if candy == 0:
            idx = 3
            tmr = 0

    if idx == 2:
        draw_txt('GAME OVER', 360, 270, 40, 'red')
        if tmr == 50:
            idx = 0

    if idx == 3:
        if stage < 3:
            draw_txt('STAGE CLAER', 360, 270, 40, 'pink')
        else:
            draw_txt('ALL STAGE CLAER', 360, 270, 40, 'violet')
        if tmr == 30:
            if stage < 3:
                stage += 1
                set_stage()
                set_char_pos()
                idx = 1
            else:
                idx = 0

    # if koff == True:
    #     key = ''
    #     koff = False
    root.after(100,main)

root = tkinter.Tk()

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
img_red = [
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red00.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red01.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red02.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red03.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red04.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red05.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red06.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red07.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red08.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red09.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red10.png'),
    tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/red11.png')
]
img_title = tkinter.PhotoImage(file='RC-SW-Games/source/pracImage/Chapter3/image_penpen/title.png')

root.title('아슬아슬 펭귄 미로')
root.resizable(False,False)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
root.bind('<Key>',key_down)
root.bind('<KeyRelease>',key_up)
set_stage()
set_char_pos()
main()
root.mainloop()