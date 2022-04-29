#!/usr/bin/python
# -*- coding:UTF-8 -*-
import tkinter as tk
import hashlib
import tkinter.messagebox
from MainPage import MainPage

class LoginFrame:
    def __init__(self,master):
        self.root = master
        self.root.geometry('320x180')
        self.root.title('登录')
        self.page = tk.Frame()
        self.page.pack()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.page).grid(row=0,column=0)
        tk.Label(self.page,text='账户：').grid(row=1,column=1,pady=10)
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=2,pady=10)

        tk.Label(self.page,text='密码：').grid(row=2,column=1,pady=10)
        tk.Entry(self.page,show='*',textvariable=self.password).grid(row=2,column=2,pady=10)

        def login():
            with open('login.txt','r',encoding='UTF-8') as login_file:
                login_info = login_file.readlines()
                for item in login_info:
                    info = dict(eval(item))
                    if info['username'] == self.username.get():
                        passwd = hashlib.md5()
                        passwd.update(self.password.get().encode('UTF-8'))
                        if info['password'] == passwd.hexdigest():
                            tk.messagebox.showinfo(title='提示',message='          登录成功          ')
                            self.page.destroy()
                            MainPage(master=master)

                        else:
                            tk.messagebox.showwarning(title='警告',message='您输入的密码或用户名有误！')
                    else:
                        tk.messagebox.showwarning(title='警告',message='您输入的密码或用户名有误！')


        tk.Button(self.page,text='登录',command=login).grid(row=3,column=2,pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    LoginFrame(master=root)
    root.mainloop()

