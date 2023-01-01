import tkinter as tk
from tkinter import ttk

w=tk.Tk()
w.title('Mallige Hotel ')
w.geometry('800x400')

options = {'padding':5,}

h1 = ttk.Label(w,text='Welcome to Mallige Hotel',font=("Helvetica", 28))
h2 = ttk.Label(w,text='Feel free to eat',font=("Helvetica", 14))
h1.place(x=100, y=10)
h2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

reg_btn=ttk.Button(w,text='Register',**options,)
ord_btn=ttk.Button(w,text='Order',**options)
cal_bil=ttk.Button(w,text='Cal_bill',**options)
reg_btn.place(relx=0.8, rely=0.3, relwidth=0.2, anchor='ne')
ord_btn.place(relx=0.8, rely=0.45, relwidth=0.2, anchor='ne')
cal_bil.place(relx=0.8, rely=0.6, relwidth=0.2, anchor='ne',)
w.mainloop()
