import tkinter
import datetime

def time_now():
    d = datetime.datetime.now() #컴퓨터의 현재시간
    t = '{0}:{1}:{2}'.format(d.hour,d.minute,d.second)
    label['text'] =t
    root.after(1000,time_now)   #1초쉬고 함수호출

root = tkinter.Tk()
root.geometry('400x100')
root.title('간이 시계')
label = tkinter.Label(font=['Times New Roman', 60, 'bold'])
label.pack()

time_now()
root.mainloop()