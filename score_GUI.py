
from posix import sched_param
from tkinter import *
from PIL import Image, ImageTk
import os
import numpy as np
import pandas as pd
import json
import tkinter.messagebox 
import requests
from io import BytesIO
 
class App:
    def __init__(self,window,w_win,h_win):
        global Pic_List
        global Index
        global img
        global img_tk
        global Index

        self.window = window
        self.w_win = w_win
        self.h_win = h_win
        self.w_canvas = 0.9*w_win
        self.h_canvas = h_win

        frame = Frame(window,width=w_win,height=h_win)
        self.frame = frame
        frame.pack()

        canvas = Canvas(frame,width=self.w_canvas,height=self.h_canvas)
        self.canvas = canvas
        canvas.place(x = 0, y = 0.5*h_win,anchor='w')

        img = Image.open(Pic_List[Index]).convert('RGB')
        # img = Image.open(BytesIO(requests.get('https://www.runoob.com/wp-content/uploads/2020/04/6C773061-44DA-4B94-8524-934664AA2425.jpg').content)).convert('RGB')
        # img.show()
        img_tk = ImageTk.PhotoImage(img)
        self.pre_imag = canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
        
        # canvas.update()

        # Index += 1
        self.label_text = StringVar()
        label = Label(textvariable=self.label_text)
        label.place(x=0.95*w_win, y=0.1*h_win, anchor='center')
        self.label_text.set(Index)

        var = DoubleVar() 
        self.var = var

        mark = Scale(frame,from_=0,  to=5,  resolution=0.1, orient=VERTICAL , variable=var ,length = int(h_win*0.4),showvalue=0,tickinterval=0.5)
        mark.place(x=0.95*w_win, y=0.5*h_win, anchor='center')
        var.set(2.5)

        next_button = Button(frame,text='Next',command=self.next)
        next_button.place(x=0.95*w_win, y=0.8*h_win, anchor='center')

        pre_button = Button(frame,text='Previous',command=self.previous)
        pre_button.place(x=0.95*w_win, y=0.2*h_win, anchor='center')

        save_button = Button(frame,text='Save',command=self.save)
        save_button.place(x=0.95*w_win, y=0.9*h_win, anchor='center')

    def next(self):
        global Pic_List
        global Index
        global Score
        global img
        global img_tk

        if Index == len(Pic_List)-1:
            print('No next')
            Score[Index] = self.var.get()
            self.var.set(2.5)
            print(Score)
            tkinter.messagebox.showwarning(message='No next') 
        else:

            Score[Index] = self.var.get()
            self.var.set(2.5)

            Index += 1
            self.label_text.set(Index)

            self.canvas.delete(self.pre_imag)

            img = Image.open(Pic_List[Index]).convert('RGB')
            # img.show()
            img_tk = ImageTk.PhotoImage(img)
            self.pre_imag = self.canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
            # print(Name)
            print(Score)
        

    def previous(self):
        global Pic_List
        global Index
        global Score
        global img
        global img_tk

        if Index == 0:
            print('No previous')
            tkinter.messagebox.showwarning(message='No previous') 
        
        else:

            Index -= 1
            self.label_text.set(Index)

            self.canvas.delete(self.pre_imag)

            img = Image.open(Pic_List[Index]).convert('RGB')
            # img.show()
            img_tk = ImageTk.PhotoImage(img)
            self.pre_imag = self.canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
            # print(Name)
    
    def save(self):
        global Score
        global Pic_List
        global Index
        global Name
        global Save_path

        with open(os.path.join(Save_path,Name+'.json'),'w') as f:
            json.dump(Score, f)

        df = pd.DataFrame(columns=['Index','Image','Score'])

        for i in range(Index + 1):
            df.loc[i] = [i,Pic_List[i].split('/')[-1],Score[i]]
        df.to_csv(os.path.join(Save_path,Name+'.csv'),index=False)

        tkinter.messagebox.showinfo(message='Thanks! '+Name) 
        self.frame.quit()



class Start:
    def __init__(self,window,w_win,h_win) -> None:
        self.window = window
        self.w_win = w_win
        self.h_win = h_win
        frame = Frame(window,width=w_win,height=h_win)
        self.frame = frame
        frame.pack()
        # frame.update()
        # print(frame.winfo_width())
        label = Label(frame,text='Please Enter your Name in English',font=('Times New Roman', 18))
        label.place(x = 0.5*w_win, y = 0.45*h_win,anchor='center')
        name = StringVar()
        self.name = name
        entry = Entry(frame,textvariable=name,font=('Times New Roman', 18))
        entry.place(x = 0.5*w_win, y = 0.5*h_win,anchor='center',width=300,height=40)
        button = Button(frame,text='Enter',command=self.save_name)
        button.place(x = 0.5*w_win, y = 0.55*h_win,anchor='center')
    def save_name(self):
        global Name
        global Index
        global Pic_List
        global Save_path
        global Score
        if self.name.get() == '':
            pass
        else:
            Name = self.name.get()
            if os.path.exists(os.path.join(Save_path,Name+'.json')):
                with open(os.path.join(Save_path,Name+'.json'),'r') as f:
                    Score = json.load(f)
                keys = list(Score.keys())
                Index = int(keys[-1])+1
                if Index >= len(Pic_List):
                    tkinter.messagebox.showwarning(message='Sorry, you have finished scoring!') 
                    self.frame.quit()
                print(Index)

            # print(self.name.get())
            self.frame.destroy()
            Introduction(self.window,self.w_win,self.h_win)

class Introduction:
    def __init__(self,window,w_win,h_win) -> None:
        global img
        global img_tk
        self.window = window
        self.w_win = w_win
        self.h_win = h_win
        frame = Frame(window,width=w_win,height=h_win)
        self.frame = frame
        frame.pack()
        # frame.update()
        # print(frame.winfo_width())
        img = Image.open('introduction.png').convert('RGB')
        size = img.size
        ratio = min(0.9*w_win/size[0],h_win/size[1])
        img = img.resize((int(size[0]*ratio),int(size[1]*ratio)))
        # img.show()
        img_tk = ImageTk.PhotoImage(img)
        label = Label(frame,image= img_tk)
        label.place(x = 0.45*w_win, y = 0.5*h_win,anchor='center')


        button = Button(frame,text='Start',command=self.start)
        button.place(x = 0.95*w_win, y = 0.5*h_win,anchor='center')
    def start(self):
        self.frame.destroy()
        App(self.window,self.w_win,self.h_win)

window = Tk()
w_win = window.winfo_screenwidth()//2
h_win = window.winfo_screenheight()
size_str = str(w_win) + 'x' + str(h_win)
# print(size_str)
window.geometry(size_str)

# global name
Image_path = 'pic'
Name = ''
Score = dict()
Save_path = 'score_data'

if not os.path.exists(Save_path):
    os.makedirs(Save_path)

Pic_List = os.listdir(Image_path)
Pic_List = [os.path.join(Image_path,i) for i in Pic_List]
# print(Pic_List)
if len(Pic_List) == 0:
    print('No pics')

Index = 0

img = None
img_tk = None

 
app = Start(window,w_win,h_win)
 
window.mainloop()
