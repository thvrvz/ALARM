import tkinter as tk 
from tkinter import ttk , messagebox 
from PIL import Image , ImageTk 
import datetime
import pygame
pygame.mixer.init()
import threading

#####Values#####

hours=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
minutes=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24',
         '25','26','27','28','29','30','31','32','33','34','35','36','36','37','38','39','40','41','42','43','44','45','46','47','48',
         '49','50','51','52','53','54','55','56','57','58','59']
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
sounds=['sound1.wav','sound2.wav','sound3.wav']


#####Defs#####

def test_alarm_play():
    global alarm_combobox
    alarm_sound=alarm_combo.get()
    sound=pygame.mixer.Sound(alarm_sound)
    sound.play(maxtime=300000)

def clock():
    time_now=datetime.datetime.now().strftime('%H:%M %p   %A')
    clock_label.config(text=datetime.datetime.now().strftime('%H:%M %p   %A'))
    clock_label.after(900,clock) 

def set_tm():
    h=hour_combo.get()
    m=min_combo.get()
    d=day_combo.get()
    
    set_time=h+':'+m+"   "+d
    now=datetime.datetime.now().strftime('%H:%M   %A')
    while set_time!=now:
        pygame.time.delay(1000)
        now=datetime.datetime.now().strftime('%H:%M   %A')
    test_alarm_play()
    messagebox.showinfo(title='ALARM!',message=msg_box.get())
    #test_alarm_play()

def setting():
    global alarm_combo,day_combo,min_combo,hour_combo,msg_box,msg_box
    win2=tk.Toplevel()
    win2.resizable(0,0)
    win2.geometry('450x400')
    win2.title('set up')
    win2.iconbitmap("S.ico")

##win2.img_bg
    img_win2=Image.open('win2.jpg')
    img_win2_rszd=img_win2.resize((450,400))
    img_win2_rszd_tk=ImageTk.PhotoImage(img_win2_rszd)
    
    bl2=tk.Label(win2,image=img_win2_rszd_tk)
    bl2.place(x=0,y=0)

##win2,combos
    tm_lable = tk.Label(win2,text=' Hour      /       Minute ',font=('Cooper Black',10),bg='deeppink2',fg='black')
    tm_lable.place(x=20,y=20,width=150,height=20)
    hour_combo=ttk.Combobox(win2,values=hours,font=('Elephant',8))
    hour_combo.place(x=20,y=50,width=60,height=25)
    hour_combo.current(00)
    min_combo=ttk.Combobox(win2,values=minutes,font=('Elephant',8))
    min_combo.place(x=90,y=50,width=60,height=25)
    min_combo.current(00)
  

    day_lable = tk.Label(win2,text='Day',font=('Cooper Black',10),bg='deeppink2',fg='black')
    day_lable.place(x=200,y=20,width=60,height=20)
    day_combo=ttk.Combobox(win2,values=days,font=('Elephant',8))
    day_combo.place(x=200,y=50,width=60,height=25)


    alarm_lable = tk.Label(win2,text='Alarm',font=('Cooper Black',10),bg='deeppink2',fg='black')
    alarm_lable.place(x=280,y=20,width=100,height=20)
    alarm_combo=ttk.Combobox(win2,values=sounds,font=('Elephant',8))
    alarm_combo.place(x=280,y=50,width=100,height=25)
    
    alarm_test=tk.Button(win2,text='Test',font=('Cooper Black',10),bg='darkorchid1',fg='black',borderwidth=1,command=test_alarm_play)
    alarm_test.place(x=395,y=20,width=40,height=20)
    

    msg_lable=tk.Label(win2,text='Alarm message',font=('Cooper Black',11),bg='deeppink2',fg='black')
    msg_lable.place(x=100,y=270)
    msg=tk.StringVar()
    msg_box=tk.Entry(win2, textvariable=msg,font=('Arial (Body CS)',11),width=20,bg='cornsilk3')
    msg_box.place(x=100,y=300)

    
    set_up=tk.Button(win2,text='SET',font=('Cooper Black',12),bg='deeppink2',fg='black',command=thread2.start)
    set_up.place(x=350,y=300)

    
    win2.mainloop()

##win1##
win1=tk.Tk()
win1.resizable(0,0)
win1.geometry("300x500")
win1.title(' MY Alarm')
win1.iconbitmap("clock.ico")

##win1.back 
img_win1=Image.open('win1.jpg')
img_win1_rszd=img_win1.resize((300,500))
img_win1_rszd_tk=ImageTk.PhotoImage(img_win1_rszd)

bl=tk.Label(win1,image=img_win1_rszd_tk)
bl.place(x=0,y=0)

clock_label=tk.Label(win1,font=('Cooper Black',16),bg='deeppink2',fg='black')
clock_label.place(x=50,y=50)
thread1=threading.Thread(target=clock)
thread2=threading.Thread(target=set_tm)
thread1.start()

setting_button=tk.Button(win1,text='SETTING',font=('Cooper Black',14),bg='deeppink2',fg='black',command=setting)
setting_button.place(x=100,y=300)







win1.mainloop()