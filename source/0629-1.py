from tkinter import *
import random
w= 400; h= 300

colors = ['white','black','red','blue','green','orange','yellow','cyan','olive','magenta','darkviolet']
vec = [-2, 0, 2]

class Ball:
    def __init__(self):
        self.y = 150                 #초기위치
        self.x = 200
        self.dx =random.choice(vec)  #방향벡터
        self.dy =random.choice(vec)
        self.color = random.choice(colors)

class MainGUI:
    def stop(self):
        self.isStoped = True
    def resume(self):
        self.isStoped = False
        self.animate()
    def add(self):
        self.ballList.append(Ball())
    def sub(self):
        self.ballList.pop()
    def fast(self):
        if self.sleep > 20:
            self.sleep -= 20
    def slow(self):
        self.sleep += 20

    def animate(self):
        while not self.isStoped:            #정지상태가 아닌동안
            self.canvas.after(self.sleep)   #멈췄다가
            self.canvas.update()            #canvas 오브젝트들을 다시 그린다
            self.canvas.delete('ball')      #지웠다가
            for ball in self.ballList:      #ballList에서 하나씩 꺼낸다
                if ball.x-5 < 0:
                    ball.dx = 2
                elif ball.x+5 > w:
                    ball.dx = -2
                if ball.y-5 < 0:
                    ball.dy = 2
                elif ball.y+5 > h:
                    ball.dy = -2
                ball.x += ball.dx
                ball.y += ball.dy
                self.canvas.create_oval(ball.x-5,ball.y-5,ball.x+5,ball.y+5,fill=ball.color,tag='ball')

    def __init__(self):
        window = Tk()
        window.title('공 튀기기')
        self.canvas = Canvas(window,width=w,height=h,bg='white')
        self.canvas.pack()
        self.ballList = []
        self.isStoped = False
        self.sleep = 100

        frame = Frame(window)
        frame.pack()
        Button(frame,text='정지',command=self.stop).pack(side=LEFT)
        Button(frame,text='재시작',command=self.resume).pack(side=LEFT)
        Button(frame,text='+',command=self.add).pack(side=LEFT)
        Button(frame,text='-',command=self.sub).pack(side=LEFT)
        Button(frame,text='빠르게',command=self.fast).pack(side=LEFT)
        Button(frame,text='느리게',command=self.slow).pack(side=LEFT)
        self.animate()
        window.mainloop()

MainGUI()