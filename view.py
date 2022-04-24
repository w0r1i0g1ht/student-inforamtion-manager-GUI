#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time
import tkinter as tk
from tkinter import ttk


class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='关于页面').pack()


class ModifyFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='修改页面').pack()

class InsertFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        # tk.Label(self,text='录入页面').pack()
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.insert_data()


    def insert_data(self):

        tk.Label(self,text='id').grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.id).grid(row=1,column=2,pady=10)
        tk.Label(self, text='姓名').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        tk.Label(self, text='语文').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)
        tk.Label(self, text='数学').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=4, column=2, pady=10)
        tk.Label(self, text='英语').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=5, column=2, pady=10)
        tk.Button(self,text='录入',command=self.save_data).grid(row=6,column=2,pady=10)




    def save_data(self):
        self.student_list = []
        self.student = {'id': self.id.get(), '姓名': self.name.get(), '语文': self.chinese.get(), '数学': self.math.get(),
                        '英语': self.english.get()}
        self.student_list.append(self.student)
        tk.Label(self, text='录入成功').grid(row=7, column=2)
        try:
            stu_txt = open('student.txt','a',encoding='UTF-8')
        except:
            stu_txt = open('student.txt','w',encoding='UTF-8')
        for item in self.student_list:
            stu_txt.write(str(item) + '\n')
        stu_txt.close()
        self.id.set('')
        self.name.set('')
        self.chinese.set('')
        self.math.set('')
        self.english.set('')




class SearchFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Button(self,text='按照id查询',command=self.id_search).pack()
        tk.Button(self,text='按照姓名查询').pack()
        self.id = tk.StringVar()
        self.name = tk.StringVar()



    def id_search(self):
        self.student_query = []
        tk.Label(self,text='id').pack()
        tk.Entry(self,textvariable=self.id).pack()
        tk.Button(self,text='查询',command=lambda:[self.show_student,self.frame_clear]).pack() # 修改到这里


    def show_student(self):

        self.table_view = tk.Frame()
        columns = ("id","name","chinese","math","english")
        columns_value = ("id","姓名","语文","数学","英语")
        self.tree_view = ttk.Treeview(self,show='headings',columns=columns)
        self.tree_view.column('id',width=80,anchor='center')
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.heading('id',text='id')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('english', text='英语')
        self.tree_view.pack(fill=tk.BOTH,expand=True)

        with open('student.txt','r',encoding='UTF-8') as id_search_file:
            student_info = id_search_file.readlines()
            for item in student_info:
                info = dict(eval(item))
                if self.id.get() !='':
                    if self.id.get() == info['id']:
                        self.student_query.append(info)
        index=0
        for item in self.student_query:
            self.tree_view.insert('',index + 1,values=(
                                  item['id'], item['姓名'], item['语文'], item['数学'], item['英语']
                                ))

    def frame_clear(self):
        self.tree_view.destroy()



class DeleteFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='删除页面').pack()

class SortFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='排序页面').pack()

class TotalFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='统计页面').pack()

class ContentFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='概览页面').pack()