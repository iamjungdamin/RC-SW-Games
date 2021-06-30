from tkinter import *

class MainGUI:
    def check(self):
        for i in range(3):
            #행 체크
            ch = self.matrix[i][0]['text']
            if ch != ' ' and ch == self.matrix[i][1]['text'] and ch == self.matrix[i][2]['text']:
                return ch
            
            #열 체크
            ch = self.matrix[0][i]['text']
            if ch != ' ' and ch == self.matrix[1][i]['text'] and ch == self.matrix[2][i]['text']:
                return ch

        #대각선 체크
        ch = self.matrix[1][1]['text']
        if ch != ' ' and ch == self.matrix[0][0]['text'] and ch == self.matrix[2][2]['text']:
            return ch
        if ch != ' ' and ch == self.matrix[0][2]['text'] and ch == self.matrix[2][0]['text']:
            return ch
        
        #게임중
        for r in range(3):
            for c in range(3):
                if self.matrix[r][c]['text'] == ' ':    #하나라도 빈칸이면
                    return ' '
        
        #비김
        return '#'

        # flag = True
        # for r in range(3):
        #     for c in range(3):
        #         if self.matrix[r][c]['text'] == ' ':    #하나라도 빈칸이면 False로
        #             flag = False
        #             break
        #     if flag == False:
        #         break

        # if flag == True:
        #     return '#'

    def pressed(self,row,col):
        if not self.done == True and self.matrix[row][col]['text'] == ' ':
            if self.turn == True:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            else:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            self.turn = not self.turn    #턴 넘김

            #승패 체크
            if self.check() == '#':
                self.explain.set('비겼습니다!')
            elif self.check() != ' ':
                self.explain.set(self.check()+'가 이겼습니다!')
                self.done = True
            elif self.turn == True:
                self.explain.set('플레이어 O 차례')
            else:
                self.explain.set('플레이어 X 차례')

    def refresh(self):
        self.turn = True
        self.done = False
        self.explain.set('플레이어 O 차례')
        for r in range(3):
            for c in range(3):
                self.matrix[r][c]['image'] = self.imageE
                self.matrix[r][c]['text'] = ' '

    def __init__(self):
        window = Tk()
        window.title('틱택토')
        self.turn = True    #True:O, Flase:X
        self.done = False
        frame = Frame(window)
        frame.pack()
        self.imageX = PhotoImage(file='RC-SW-Games/source/image/x.gif')
        self.imageO = PhotoImage(file='RC-SW-Games/source/image/o.gif')
        self.imageE = PhotoImage(file='RC-SW-Games/source/image/empty.gif')
        self.matrix = []
        for r in range (3):
            self.matrix.append([])  #[ [B,B,B], [B,B,B], [B,B,B] ]
            for c in range(3):
                self.matrix[r].append(Button(frame,image=self.imageE,text =' ',
                                      command=lambda row=r, col=c: self.pressed(row,col)))
                self.matrix[r][c].grid(row=r, column=c)
        self.explain = StringVar()
        self.explain.set('플레이어 O 차례')
        Label(window,textvariable=self.explain).pack()
        Button(window,text='다시 시작',command=self.refresh).pack()
        window.mainloop()

MainGUI()