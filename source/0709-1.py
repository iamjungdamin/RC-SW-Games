from tkinter import *
import random

TILE_SIZE = 24

colors = [
    'azure4',
    'red',
    'green',
    'blue',
    'purple',
    'yellow',
    'cyan',
    'magenta'
]
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

class TetrisApp:
    def help(self):
        self.canvas = Canvas(self.window, width=TILE_SIZE * self.cols, height=TILE_SIZE * self.rows, bg='black')
        self.canvas.pack(side='left')
        self.canvas.create_text(100,50,text='TETRIS', font=('arial',24), anchor='center', fill='orange')
        self.canvas.create_text(10,100,text='Up: rotate', font=('arial',16), anchor='w', fill='white')
        self.canvas.create_text(10,130,text='Left: move left', font=('arial',16), anchor='w', fill='white')
        self.canvas.create_text(10,160,text='Right: move right', font=('arial',16), anchor='w', fill='white')
        self.canvas.create_text(10,190,text='Down: move down', font=('arial',16), anchor='w', fill='white')
        self.canvas.create_text(10,220,text='p: pause', font=('arial',16), anchor='w', fill='white')
        self.canvas.create_text(10,250,text='Space: start', font=('arial',16), anchor='w', fill='white')

    def check_collision(self,offset):
        # 예 self.stone = [[0, 2, 2],
        #                  [2, 2, 0]]
        off_x, off_y = offset
        for y, row in enumerate(self.stone):
            for x, val in enumerate(row):
                if 0 <= y+off_y < self.rows and 0<= x+off_x < self.cols:#유효한 인덱스 검사
                    if val and self.gridCell[y+off_y][x+off_x]:         #스톤도 비어있지않고 보드도 비어있지않으면
                        return True
                else:
                    return True

        return False

    # self.stone을 self.board에 추가
    def merge_stone(self):
        # 예 self.stone = [[0, 2, 2],
        #                  [2, 2, 0]]
        for y, row in enumerate(self.stone):
            for x, val in enumerate(row):
                if val:
                    self.gridCell[y+self.stone_y][x+self.stone_x] = val

    def new_stone(self):
        #7개 tetris 중에서 랜덤으로 하나 선택
        self.stone = tetris_shapes[random.randrange(len(tetris_shapes))]

        #stone x 위치 = 게임판 중간(self.cols/2) -  stone 의 너비의 절반(self.stone[0]/2)
        self.stone_x = self.cols//2 - len(self.stone[0])//2
        #stone y 위치
        self.stone_y = 0

        if self.check_collision((self.stone_x,self.stone_y)):
            self.gameover = True

    def init_game(self):
        #2D 격자 숫자 생성 (0 비어 있는 셀)
        self.gridCell = [[0 for x in range(self.cols)]
                            for y in range(self.rows)]

        #2D 격자 라벨 생성
        self.board = []
        for r in range(self.rows):
            temp = []
            for c in range(self.cols):
                l = Label(self.frame,text='',bg='azure4',width=2,height=1)
                l.grid(row=r,column=c,padx=1,pady=1) #r행 c열 격자 라벨 생성
                temp.append(l)
            self.board.append(temp)
        self.new_stone()

    #2D 격자 라벨(self.board)의 배경색과 숫자색 칠하기
    def paintGrid(self):
        #self.board 각 셀들의 라벨 색 칠하기
        for r in range(self.rows):
            for c in range(self.cols):
                if self.gridCell[r][c] == 0:    #셀이 비어 있으면
                    self.board[r][c].configure(text='',bg='azure4')
                else:
                    self.board[r][c].configure(text='',
                                               bg=colors[self.gridCell[r][c]])
        #self.stone 라벨 색 칠하기
        for y, row in enumerate(self.stone):  # 인덱스와 값을 추출, (y,row)=(0,[0,2,2]), (1,[2,2,0])
            for x, val in enumerate(row):  # (x,col) = (0,0), (1,2), (2,2)
                if val: #빈 셀이 아니라면
                    self.board[y + self.stone_y][x + self.stone_x].configure(text='',
                                                                  bg=colors[self.stone[y][x]])

    # 키 입력 Up, Down, Left, Right, P, Space 이벤트 처리 함수
    def link_keys(self,event):
        key = event.keysym
        if key == 'p':
            self.pause = not self.pause

        if self.gameover or self.pause:   #게임 종료 혹은 Pause이면 키 입력 처리 안함
            return

        if key == 'Up':
            self.rotate()
        elif key == 'Down':
            self.move_down()
        elif key == 'Left':
            self.move_left()
        elif key == 'Right':
            self.move_right()
        elif key == 'space':
            self.main()
        else:
            pass

    def rotate(self):
        # 예 self.stone = [[1, 1, 1],
        #                  [0, 1, 0]]

        # y좌표는 1, 0, x좌표는 2, 1, 0 즉 2열의 2개, 1열의 2개, 0열의 2개 묶음
        # rotate_left:    [[1, 0],
        #                  [1, 1],
        #                  [1, 0]]
        # [self.stone[y][x] for y in range(len(self.stone))] for x in range(len(self.stone[0]-1,-1,-1))]

        # y좌표는 0, 1, x좌표는 0, 1, 2 즉 0열의 2개, 1열의 2개, 2열의 2개 묶음
        # rotate_right:   [[0, 1],
        #                  [1, 1],
        #                  [0, 1]]
        # [self.stone[y][x] for y in range(len(self.stone)-1,-1,-1)] for x in range(len(self.stone[0]))]

        # 참고로 전치행렬은
        # [self.stone[y][x] for y in range(len(self.stone))] for x in range(len(self.stone[0]))]

        self.stone = [ [self.stone[y][x] for y in range(len(self.stone))] for x in range(len(self.stone[0]) -1,-1,-1) ]

        if self.check_collision( (self.stone_x,self.stone_y) ):
            self.stone = [ [self.stone[y][x] for y in range(len(self.stone)-1,-1,-1)] for x in range(len(self.stone[0]))]
        else:
            self.paintGrid()

    def check_remove(self):
        # 맨 밑줄에서 부터 rows-1,...0 으로 한줄이 채워졌으면 없애고 self.board 앞에 [0,0,0,0,...0]을 붙임
        i = self.rows-1
        while i >= 0:
            if not 0 in self.gridCell[i]:
                del (self.gridCell[i])
                self.gridCell = [ [0 for _ in range(self.cols)] ] + self.gridCell
            else:   #채워지지 않았으면 1 감소 (바로 윗줄 검사)
                i -= 1

    def move_down(self):
        if self.check_collision((self.stone_x,self.stone_y+1)):
            self.merge_stone()
            self.new_stone()
            self.check_remove()
        else:
            self.stone_y += 1
        self.paintGrid()

    def move_left(self):
        if not self.check_collision((self.stone_x-1,self.stone_y)):
            self.stone_x -= 1
            self.paintGrid()

    def move_right(self):
        if not self.check_collision((self.stone_x+1,self.stone_y)):
            self.stone_x += 1
            self.paintGrid()

    def main(self):
        if not (self.gameover or self.pause):
            self.paintGrid()
            self.move_down()
        self.window.after(300,self.main)

    def __init__(self,w,h):
        self.cols = w
        self.rows = h
        self.gameover = False
        self.pause = False
        self.window = Tk()
        self.window.geometry('%dx%d'%(TILE_SIZE*self.cols*2, TILE_SIZE*self.rows))
        self.window.resizable(False,False)
        self.window.title('테트리스')
        self.frame = Frame(self.window, width=TILE_SIZE*self.cols,height=TILE_SIZE*self.rows, bg='black')
        self.frame.pack(side='left')

        self.help() #키 입력 설명
        self.init_game()
        self.window.bind('<Key>',self.link_keys) #키입력 이벤트 함수 self.link_keys 연결
        self.window.mainloop()

TetrisApp(8,16)
#TetrisApp(10,20)
