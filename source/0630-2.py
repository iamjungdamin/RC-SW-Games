from tkinter import *

class MainGUI:
    def check(self):
        #가로 4개씩 검사
        for r in range(6):
            for c in range(4):  # 0,1,2,3 (c == c+1 == c+2 == c+3)
                ch = self.matrix[r][c]['text']
                if ch != ' ' and ch == self.matrix[r][c+1]['text'] and ch == self.matrix[r][c+2]['text'] \
                    and ch == self.matrix[r][c+3]['text']:
                    return ch

        #세로 4개씩 검사
        for r in range(3):      # 0,1,2 (r == r+1 == r+2 == r+3)
            for c in range(7):
                ch = self.matrix[r][c]['text']
                if ch != ' ' and ch == self.matrix[r+1][c]['text'] and ch == self.matrix[r+2][c]['text'] \
                    and ch == self.matrix[r+3][c]['text']:
                    return ch

        #대각선 검사
        #우하향
        for r in range(3):      # 0,1,2
            for c in range(4):  # 0,1,2,3
                ch = self.matrix[r][c]['text']
                if ch != ' ' and ch == self.matrix[r+1][c+1]['text'] and ch == self.matrix[r+2][c+2]['text'] \
                    and ch == self.matrix[r+3][c+3]['text']:
                    return ch

        #좌하향
        for r in range(3):      # 0,1,2
            for c in range(3,7):# 3,4,5,6 (c == c-1 == c-2 == c-3)
                ch = self.matrix[r][c]['text']
                if ch != ' ' and ch == self.matrix[r+1][c-1]['text'] and ch == self.matrix[r+2][c-2]['text'] \
                    and ch == self.matrix[r+3][c-3]['text']:
                    return ch

        return ' '

    def pressed(self,col):
        for row in range(5, -1, -1): #5,4,3,2,1,0
            if not self.done == True and self.matrix[row][col]['text'] == ' ':
                if self.turn == True:
                    self.matrix[row][col]['image'] = self.imageO
                    self.matrix[row][col]['text'] = 'O'
                else:
                    self.matrix[row][col]['image'] = self.imageX
                    self.matrix[row][col]['text'] = 'X'
                self.turn = not self.turn

                if self.check() == '#':
                    self.explain.set('비겼습니다!')
                    self.done = True
                elif self.check() != ' ':
                    self.explain.set(self.check()+'가 이겼습니다!')
                    self.done = True
                elif self.turn == True:
                    self.explain.set('플레이어 O 차례')
                else:
                    self.explain.set('플레이어 X 차례')
                
                # 한개만 놓고
                break

    def refresh(self):
        self.turn = True
        self.done = False
        self.explain.set('플레이어 O 차례')
        for r in range(6):
            for c in range(7):
                self.matrix[r][c]['image'] = self.imageE
                self.matrix[r][c]['text'] = ' '

    def __init__(self):
        window = Tk()
        window.title('사목게임')
        self.imageX = PhotoImage(file='RC-SW-Games/source/image/x.gif')
        self.imageO = PhotoImage(file='RC-SW-Games/source/image/o.gif')
        self.imageE = PhotoImage(file='RC-SW-Games/source/image/empty.gif')
        frame = Frame(window)
        frame.pack()
        self.turn = True
        self.done = False

        self.matrix = []
        for r in range(6):
            self.matrix.append([])
            for c in range(7):
                self.matrix[r].append(Button(frame,text= ' ',image=self.imageE,
                                      command=lambda col=c:self.pressed(col)))
                self.matrix[r][c].grid(row=r,column=c)

            self.explain = StringVar()
            self.explain.set('플레이어 O 차례')
            Label(window,textvariable=self.explain).pack()
            Button(window,text='새로시작',command=self.refresh).pack()
            window.mainloop()
    
MainGUI()