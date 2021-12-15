
# from posix import sched_param
from tkinter import *
from PIL import Image, ImageTk
import os
import numpy as np
import pandas as pd
import json
import tkinter.messagebox 
import requests
from io import BytesIO
import argparse

def arg():
    parser = argparse.ArgumentParser()

    # input parameters
    parser.add_argument('--img_path', type=str,default='pic')
    parser.add_argument('--csv_file', type=str,default='Images.csv')
    parser.add_argument('--mode', type=str,default='local',choices=['local','internet'])

    config = parser.parse_args()

    return config
 

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
        entry.focus_set()
        button = Button(frame,text='Enter',command=self.save_name)
        button.place(x = 0.5*w_win, y = 0.55*h_win,anchor='center')
        entry.bind("<Return>",self.save_name_key)
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
                    score = json.load(f)
                keys = list(score.keys())
                index = int(keys[-1])+1
                if index >= len(Pic_List):
                    tkinter.messagebox.showwarning(message='Sorry, you have finished scoring!') 
                    # self.frame.quit()
                # print(Index)
                else:
                    Index = index
                    Score = score
                    self.frame.destroy()
                    Introduction(self.window,self.w_win,self.h_win)
            else:
                # print(self.name.get())
                self.frame.destroy()
                Introduction(self.window,self.w_win,self.h_win)
    def save_name_key(self,event):
        self.save_name()

class Introduction:
    def __init__(self,window,w_win,h_win) -> None:
        global img
        global img_tk
        self.window = window
        self.w_win = w_win
        self.h_win = h_win
        frame = Frame(window,width=w_win,height=h_win)
        frame.focus_set()
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

        frame.bind("<Return>",self.start_key)
    def start(self):
        self.frame.destroy()
        App(self.window,self.w_win,self.h_win)
    def start_key(self,event):
        self.start()

class App:
    def __init__(self,window,w_win,h_win):
        global Pic_List
        global Index
        global img
        global img_tk
        global Index
        global Mode

        self.window = window
        self.w_win = w_win
        self.h_win = h_win
        self.w_canvas = 0.9*w_win
        self.h_canvas = h_win

        frame = Frame(window,width=w_win,height=h_win)
        self.frame = frame
        frame.focus_set()
        frame.pack()

        canvas = Canvas(frame,width=self.w_canvas,height=self.h_canvas)
        self.canvas = canvas
        canvas.place(x = 0, y = 0.5*h_win,anchor='w')
        if Mode == 'local':
            img = Image.open(Pic_List[Index]).convert('RGB')
        elif Mode == 'internet':
            img = Image.open(BytesIO(requests.get(Pic_List[Index]).content)).convert('RGB')
        size = img.size
        if max(size[0],size[1]) > 3000:
            ratio = max(1080/size[0],1080/size[1])
            img = img.resize((int(size[0]*ratio),int(size[1]*ratio)))
        # img.show()
        img_tk = ImageTk.PhotoImage(img)
        self.pre_imag = canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
        
        # canvas.update()

        # Index += 1
        self.label_text = StringVar()
        label = Label(frame,textvariable=self.label_text,font=('Times New Roman', 18))
        label.place(x=0.95*w_win, y=0.1*h_win, anchor='center')
        self.label_text.set("Index: {}".format(Index))

        var = DoubleVar() 
        self.var = var

        mark = Scale(frame,from_=5,  to=0,  resolution=0.1, orient=VERTICAL , variable=var ,length = int(h_win*0.4),showvalue=0,tickinterval=0.5)
        mark.place(x=0.95*w_win, y=0.5*h_win, anchor='center')
        window.bind("<MouseWheel>", self.wheel)
        window.bind("<Button-4>",self.wheel_up)
        window.bind("<Button-5>",self.wheel_down)
        var.set(2.5)

        self.label_scale_text = StringVar()
        label_scale = Label(frame,textvariable=self.label_scale_text,font=('Times New Roman', 18))
        label_scale.place(x=0.95*w_win, y=0.75*h_win, anchor='center')
        self.label_scale_text.set(round(var.get(),1))

        next_button = Button(frame,text='Next',command=self.next)
        next_button.place(x=0.95*w_win, y=0.8*h_win, anchor='center')

        pre_button = Button(frame,text='Previous',command=self.previous)
        pre_button.place(x=0.95*w_win, y=0.2*h_win, anchor='center')

        save_button = Button(frame,text='Save',command=self.save)
        save_button.place(x=0.95*w_win, y=0.9*h_win, anchor='center')


        frame.bind("<Left>",self.previous_key)
        frame.bind("<Right>",self.next_key)
        # frame.bind("<Button-1>",self.previous_key)
        window.bind("<Button-3>",self.next_key)
        frame.bind("<Up>",self.wheel_up)
        frame.bind("<Down>",self.wheel_down)

    def wheel(self,event):
        # print('haha')
        # print(event.delta)
        if event.delta > 0:
            self.var.set(self.var.get()+0.1)
            self.label_scale_text.set(round(self.var.get(),1))
        else:
            self.var.set(self.var.get()-0.1)
            self.label_scale_text.set(round(self.var.get(),1))
    def wheel_up(self,event):
        # print('haha')
        self.var.set(self.var.get()+0.1)
        self.label_scale_text.set(round(self.var.get(),1))

    def wheel_down(self,event):

        self.var.set(self.var.get()-0.1)
        self.label_scale_text.set(round(self.var.get(),1))

    def next(self):
        global Pic_List
        global Index
        global Score
        global img
        global img_tk

        if Index == len(Pic_List)-1:
            #print('No next')
            Score[str(Index)] = round(self.var.get(),1)
            self.var.set(2.5)
            self.label_scale_text.set(round(self.var.get(),1))
            # print(Score)
            tkinter.messagebox.showwarning(message="No next, Please click the 'save' button to end the scoring.") 
        else:
            # self.frame.destroy()
            Score[str(Index)] = round(self.var.get(),1)
            self.var.set(2.5)
            self.label_scale_text.set(round(self.var.get(),1))

            Index += 1
            self.label_text.set("Index: {}".format(Index))

            self.canvas.delete(self.pre_imag)

            if Mode == 'local':
                img = Image.open(Pic_List[Index]).convert('RGB')
            elif Mode == 'internet':
                img = Image.open(BytesIO(requests.get(Pic_List[Index]).content)).convert('RGB')
            size = img.size
            if max(size[0],size[1]) > 3000:
                ratio = max(1080/size[0],1080/size[1])
                img = img.resize((int(size[0]*ratio),int(size[1]*ratio)))

            # img = Image.open(Pic_List[Index]).convert('RGB')
            # img.show()
            img_tk = ImageTk.PhotoImage(img)
            self.pre_imag = self.canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
            # print(Name)
            # print(Score)
    def next_key(self, event):
        self.next()

    def previous(self):
        global Pic_List
        global Index
        global Score
        global img
        global img_tk

        if Index == 0:
            #print('No previous')
            tkinter.messagebox.showwarning(message='No previous') 
        
        else:

            Index -= 1
            self.label_text.set("Index: {}".format(Index))
            self.var.set(Score[str(Index)])
            self.label_scale_text.set(round(self.var.get(),1))

            self.canvas.delete(self.pre_imag)

            # img = Image.open(Pic_List[Index]).convert('RGB')
            if Mode == 'local':
                img = Image.open(Pic_List[Index]).convert('RGB')
            elif Mode == 'internet':
                img = Image.open(BytesIO(requests.get(Pic_List[Index]).content)).convert('RGB')
            size = img.size
            if max(size[0],size[1]) > 3000:
                ratio = max(1080/size[0],1080/size[1])
                img = img.resize((int(size[0]*ratio),int(size[1]*ratio)))
            # img.show()
            img_tk = ImageTk.PhotoImage(img)
            self.pre_imag = self.canvas.create_image(self.w_canvas//2,self.h_canvas//2,anchor=CENTER,image = img_tk)
            # print(Name)
    def previous_key(self, event):
        self.previous()
    
    def save(self):
        global Score
        global Pic_List
        global Index
        global Name
        global Save_path

        if Index == 0:
            tkinter.messagebox.showwarning(message='No score record!') 
        
        else:

            with open(os.path.join(Save_path,Name+'.json'),'w') as f:
                json.dump(Score, f)

            df = pd.DataFrame(columns=['Index','Image','Score'])

            for i in range(Index + 1):
                try:
                    # print(i)
                    # df.loc[i] = [i,Pic_List[i].split('/')[-1],Score[str(i)]]
                    df.loc[i] = [i,os.path.split(Pic_List[i])[-1],Score[str(i)]]
                except:
                    pass
            df.to_csv(os.path.join(Save_path,Name+'.csv'),index=False)

            tkinter.messagebox.showinfo(message='Thanks! '+Name) 
            # self.frame.quit()


if __name__ == '__main__':

    config = arg()

    window = Tk()
    window.title('Subjective Quality Assessment for Computer Generated Images')
    w_win = window.winfo_screenwidth()
    h_win = window.winfo_screenheight()
    size_str = str(w_win) + 'x' + str(h_win)
    # print(size_str)
    # add test point
    window.geometry(size_str)
    window.attributes("-topmost",True)
    Mode = config.mode
    # global name
    # Image_path = 'http://0.0.0.0:80/pic'
    # #python -m http.server 80
    Image_path = config.img_path
    if config.mode == 'local' and not os.path.exists(Image_path):
        raise Exception('img_path does not exist!')
    if config.mode == 'internet' and Image_path[:4] != 'http':
        raise Exception('Please provide http address in Internet mode')
    Name = ''
    Score = dict()
    Save_path = 'score_data'

    if not os.path.exists(Save_path):
        os.makedirs(Save_path)

    # Pic_List = os.listdir(Image_path)
    # Pic_List = [os.path.join(Image_path,i) for i in Pic_List]
    if not os.path.exists(config.csv_file):
        raise Exception('csv_file does not exist!')
    df = pd.read_csv(config.csv_file)
    Pic_List_tmp = np.array(df['Image'])
    Pic_List = [os.path.join(Image_path,i) for i in Pic_List_tmp]

    # print(Pic_List)
    if len(Pic_List) == 0:
        print('No pics')
        raise Exception('No pics')
    if config.mode == 'local' and not os.path.exists(Pic_List[0]):
        raise Exception('{} does not exist!'.format(Pic_List[0]))

    Index = 0

    img = None
    img_tk = None

    
    app = Start(window,w_win,h_win)
    
    window.mainloop()
