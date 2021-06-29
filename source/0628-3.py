from tkinter import *
w=400; h=300

class Ball:
    def __init__(self):
        self.x = 10
        self.y = 10

class MainGUI:
    def up(self):
        if self.ball.y > 5:
            self.ball.y -= 5
            self.canvas.delete('ball') #tags가 'ball'인 객체 지운다
            self.canvas.create_oval(self.ball.x-5, self.ball.y-5, self.ball.x+5, self.ball.y+5,
                                fill='red',tags='ball')

    def down(self):
        if self.ball.y < h-5:
            self.ball.y += 5
            self.canvas.delete('ball') #tags가 'ball'인 객체 지운다
            self.canvas.create_oval(self.ball.x-5, self.ball.y-5, self.ball.x+5, self.ball.y+5,
                                fill='red',tags='ball')
    
    def left(self):
        if self.ball.x > 5:
            self.ball.x -= 5
            self.canvas.delete('ball') #tags가 'ball'인 객체 지운다
            self.canvas.create_oval(self.ball.x-5, self.ball.y-5, self.ball.x+5, self.ball.y+5,
                                fill='red',tags='ball')
    
    def right(self):
        if self.ball.x < w-5:
            self.ball.x += 5
            self.canvas.delete('ball') #tags가 'ball'인 객체 지운다
            self.canvas.create_oval(self.ball.x-5, self.ball.y-5, self.ball.x+5, self.ball.y+5,
                                fill='red',tags='ball')

    def __init__(self):
        window = Tk()
        window.title("공 옮기기")
        self.canvas = Canvas(window,width=w,height=h,bg='white') #self붙이면 멤버변수
        self.canvas.pack()
        self.ball = Ball()
        self.canvas.create_oval(self.ball.x-5, self.ball.y-5, self.ball.x+5, self.ball.y+5,
                                fill='red',tags='ball')
        frame = Frame(window)
        frame.pack()
        Button(frame,text='상',command=self.up).pack(side=LEFT)   
        Button(frame,text='하',command=self.down).pack(side=LEFT)
        Button(frame,text='좌',command=self.left).pack(side=LEFT)
        Button(frame,text='우',command=self.right).pack(side=LEFT)     
        window.mainloop()

MainGUI()