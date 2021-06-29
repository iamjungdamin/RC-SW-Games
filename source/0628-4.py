from tkinter import *
w = 600; h= 200

class MainGUI:
    def display(self):
        self.canvas.delete('shape') #tags가 shape인 오브젝트 지우기
        if self.filled.get() ==1: #채움
            if self.v.get() ==1:
                self.canvas.create_rectangle(10,10,w-10,h-10,fill='blue',tags='shape')
            else:
                self.canvas.create_oval(10,10,w-10,h-10,fill='blue',tags='shape')
        else: #안채움
            if self.v.get() ==1:
                self.canvas.create_rectangle(10,10,w-10,h-10,tags='shape')
            else:
                self.canvas.create_oval(10,10,w-10,h-10,tags='shape')

    def __init__(self):
        window = Tk()
        window.title('라디오 버튼과 체크 버튼')
        self.canvas = Canvas(window, width=w, height=h, bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame,text='직사각형',variable=self.v, value=1, command=self.display).pack(side=LEFT)
        Radiobutton(frame,text='타원',variable=self.v, value=2, command=self.display).pack(side=LEFT)
        self.filled = IntVar()
        Checkbutton(frame,text='채우기',variable=self.filled,command=self.display).pack(side=LEFT)
        window.mainloop()

MainGUI()