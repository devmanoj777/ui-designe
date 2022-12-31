import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

w=tk.Tk()

w.geometry('800x600+50+50')
w.title('dev app')
w.attributes('-topmost',1)


def download_clicked():
    showinfo(
        title='information',
        message='dowloaded successfully'
    )


lable=ttk.Label(w,text='Welcome to tk-inter').pack()
lable=ttk.Label(w,text='login to your app').pack()

btn_download=ttk.Button(w,text='Download',command=download_clicked).pack()
btn=ttk.Button(w,text='exit',command=lambda:w.quit())


btn.pack(ipadx='5',ipady='5',expand=True)

w.mainloop()