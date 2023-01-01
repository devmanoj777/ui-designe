import tkinter as tk
from tkinter import ttk
w=tk.Tk()
w.title('Register-Mallige Hotel')
w.geometry('800x400')
w.resizable(0,0)

w.columnconfigure(index=0,weight=2)
w.columnconfigure(index=1,weight=4)
h1 = ttk.Label(w,text='Register to get Daily Serviece ',font=('Helvetica',20)).pack()
name=ttk.Label(w,text='Name :').grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
e1= ttk.Entry().grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
Phone_no=ttk.Label(w,text='Phone No :').pack()
e2 = ttk.Entry().pack()
email=ttk.Label(w,text='Email :').pack()
e3 = ttk.Entry().pack()


w.mainloop()
