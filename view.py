#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import tkinter as tk
from tkinter import ttk


class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='关于页面').pack()
        tk.Label(self,text='made by 丘丘人之大都督').pack()
        tk.Label(self,text='可实现功能有：1.录入 2.查询 3.修改 4.删除 5.排序 6.概览 7.统计 8.关于').pack()



class ModifyFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.flag = tk.StringVar()
        self.student_query = []
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.modify_page()

    def modify_page(self):
        tk.Label(self, text='id：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=1, column=2, pady=10)
        tk.Label(self, text='姓名：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        tk.Label(self, text='语文：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)
        tk.Label(self, text='数学：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=4, column=2, pady=10)
        tk.Label(self, text='英语：').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=5, column=2, pady=10)
        tk.Button(self, text='查询', command=self.search_data).grid(row=6, column=1, pady=10)
        tk.Button(self, text='修改', command=self.modify_data).grid(row=6, column=3, pady=10)
        tk.Label(self,textvariable=self.status).grid(row=7, column=2, pady=10)


    def search_data(self):
        self.flag = False
        if os.path.exists('student.txt'):
            with open('student.txt','r',encoding='UTF-8') as id_search_file:
                student_info = id_search_file.readlines()
        else:
            self.status.set('存放信息的文件不存在')
        for item in student_info:
            info = dict(eval(item))
            if self.id.get() !='':
                if self.id.get() == info['id']:
                    self.student_query.append(info)
                    self.flag = True
        if self.flag:
            for item in self.student_query:
                self.id.set(item['id'])
                self.name.set(item['姓名'])
                self.chinese.set(item['语文'])
                self.math.set(item['数学'])
                self.english.set(item['英语'])
                self.status.set('数据查询成功')
        else:
            self.status.set('未查询到此人')
            self.name.set('')
            self.chinese.set('')
            self.math.set('')
            self.english.set('')
        self.student_query = []
        pass

    def modify_data(self):
        if self.id.get() != '':
            if os.path.exists('student.txt'):
                with open('student.txt','r',encoding='UTF-8') as r_file:
                    student_info = r_file.readlines()
            else:
                self.status.set('存放信息的文件不存在')

            if student_info:
                with open('student.txt','w',encoding='UTF-8') as w_file:
                    flag = False
                    for item in student_info:
                        info = dict(eval(item))
                        if info['id'] != self.id.get():
                            w_file.write(str(info) + '\n')
                        else:
                            info['姓名'] = self.name.get()
                            info['语文'] = self.chinese.get()
                            info['数学'] = self.math.get()
                            info['英语'] = self.english.get()
                            w_file.write(str(info) + '\n')
                            flag = True
                    if flag:
                        self.status.set(f'id为{self.id.get()}的学生已被修改')
                        self.name.set('')
                        self.chinese.set('')
                        self.math.set('')
                        self.english.set('')
                    else:
                        self.status.set(f'没有找到id为{self.id.get()}的学生')

        else:
            self.status.set('请输入要删除的id')
        pass





class InsertFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.insert_page()


    def insert_page(self):

        tk.Label(self,text='id：').grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.id).grid(row=1,column=2,pady=10)
        tk.Label(self, text='姓名：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        tk.Label(self, text='语文：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)
        tk.Label(self, text='数学：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=4, column=2, pady=10)
        tk.Label(self, text='英语：').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=5, column=2, pady=10)
        tk.Button(self,text='录入',command=self.save_data).grid(row=6,column=2,pady=10)
        tk.Label(self, textvariable=self.status).grid(row=7, column=2)



    def save_data(self):
        if self.id.get() != '':
            self.student_list = []
            self.student = {'id': self.id.get(), '姓名': self.name.get(), '语文': self.chinese.get(), '数学': self.math.get(),
                            '英语': self.english.get()}
            self.student_list.append(self.student)
            self.status.set('录入成功')
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
        else:
            self.status.set('id为必填项')




class SearchFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.student_query = []
        self.id_Button = tk.Button(self,text='按照id查询',command=self.id_search)
        self.id_Button.pack()
        # tk.Button(self,text='按照姓名查询').pack()   思路： id和姓名各自创建一个frame
        self.id = tk.StringVar()
        self.name = tk.StringVar()



    def id_search(self):
        tk.Label(self,text='请输入id').pack()
        tk.Entry(self,textvariable=self.id).pack()
        self.Button1 = tk.Button(self,text='查询',command=self.show_student)
        self.Button1.pack()
        self.id_Button.destroy()

    def show_student(self):

        self.table_view = tk.Frame()
        columns = ("id","name","chinese","math","english")
        columns_value = ("id","姓名","语文","数学","英语")
        self.tree_view = ttk.Treeview(self,show='headings',columns=columns)
        self.tree_view.column('id',width=80,anchor='center')
        self.tree_view.column('name', width=120, anchor='center')
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
        self.Button1.destroy()
        tk.Button(self,text='继续查询',command=self.show_student2).pack()

    def show_student2(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        with open('student.txt','r',encoding='UTF-8') as id_search_file:
            student_info = id_search_file.readlines()
            for item in student_info:
                info = dict(eval(item))
                if self.id.get() !='':
                    if self.id.get() == info['id']:
                        self.student_query=[]
                        self.student_query.append(info)
        index = 0
        for item in self.student_query:
            self.tree_view.insert('',index + 1,values=(
                                  item['id'], item['姓名'], item['语文'], item['数学'], item['英语']
                                ))



class DeleteFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.id = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self,text='根据id删除用户').pack()
        tk.Entry(self,textvariable=self.id).pack()
        tk.Button(self,text='删除',command=self.id_delete).pack()
        tk.Label(self,textvariable=self.status).pack()

    def id_delete(self):
        student_info = []
        if self.id.get() != '':
            if os.path.exists('student.txt'):
                with open('student.txt','r',encoding='UTF-8') as r_file:
                    student_info = r_file.readlines()
            else:
                self.status.set('存放信息的文件不存在')

            if student_info:
                with open('student.txt','w',encoding='UTF-8') as w_file:
                    info = []
                    flag = False
                    for item in student_info:
                        info = dict(eval(item))
                        if info['id'] != self.id.get():
                            w_file.write(str(info) + '\n')
                        else:
                            flag = True
                    if flag:
                        self.status.set(f'id为{self.id.get()}的学生已被删除')
                    else:
                        self.status.set(f'没有找到id为{self.id.get()}的学生')

        else:
            self.status.set('请输入要删除的id')
        pass




class SortFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='排序页面').grid(row=1,column=2,pady=10)
        tk.Button(self,text='按照语文成绩排序').grid(row=2,column=1,pady=10)
        tk.Button(self,text='按照数学成绩排序').grid(row=2,column=2,pady=10)
        tk.Button(self,text='按照英语成绩排序').grid(row=2,column=3,pady=10)






class TotalFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.student_query = []
        self.Total_page()


    def Total_page(self):
        self.table_view = tk.Frame()
        columns = ("chinese_aver","math_aver","english_aver","score_aver")
        columns_value = ("语文平均分","数学平均分","英语平均分","总成绩平均分")
        self.tree_view = ttk.Treeview(self,show='headings',columns=columns)
        self.tree_view.column('chinese_aver',width=100,anchor='center')
        self.tree_view.column('math_aver', width=100, anchor='center')
        self.tree_view.column('english_aver', width=100, anchor='center')
        self.tree_view.column('score_aver', width=100, anchor='center')
        self.tree_view.heading('chinese_aver',text='语文平均分')
        self.tree_view.heading('math_aver', text='数学平均分')
        self.tree_view.heading('english_aver', text='英语平均分')
        self.tree_view.heading('score_aver', text='总成绩平均分')
        self.tree_view.pack(fill=tk.BOTH,expand=True)

        with open('student.txt','r',encoding='UTF-8') as search_file:
            student_info = search_file.readlines()
            index = 1
            chinese_total = 0
            math_total = 0
            english_total = 0
            score_total = 0
            length = 0
            self.student_query = []
            for item in student_info:
                info = dict(eval(item))
                self.student_query.append(info)
            for item in self.student_query:
                chinese_total += int(item['语文'])
                math_total += int(item['数学'])
                english_total += int(item['英语'])
                length += 1
            score_total += chinese_total + math_total + english_total
            self.tree_view.insert('', index + 1, values=(
                chinese_total/length, math_total/length, english_total/length, score_total/length
            ))
        tk.Button(self, text='刷新', command=self.Total_page2).pack()



    def Total_page2(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        with open('student.txt','r',encoding='UTF-8') as search_file:
            student_info = search_file.readlines()
            index = 1
            chinese_total = 0
            math_total = 0
            english_total = 0
            score_total = 0
            length = 0
            self.student_query = []
            for item in student_info:
                info = dict(eval(item))
                self.student_query.append(info)
            for item in self.student_query:
                chinese_total += int(item['语文'])
                math_total += int(item['数学'])
                english_total += int(item['英语'])
                length += 1
            score_total += chinese_total + math_total + english_total
            self.tree_view.insert('', index + 1, values=(
                chinese_total/length, math_total/length, english_total/length, score_total/length
            ))
        pass


class ContentFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.show_content()

    def show_content(self):
        self.table_view = tk.Frame()
        columns = ("id", "name", "chinese", "math", "english", "total")
        columns_value = ("id", "姓名", "语文", "数学", "英语", "总成绩")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('name', width=120, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.column('total', width=80, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文', command=lambda col="chinese": self.tree_view_sort_column(col,False))
        self.tree_view.heading('math', text='数学', command=lambda col="math": self.tree_view_sort_column(col,False))
        self.tree_view.heading('english', text='英语', command=lambda col="english": self.tree_view_sort_column(col,False))
        self.tree_view.heading('total', text='总成绩', command=lambda col="total": self.tree_view_sort_column(col,False))
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        with open('student.txt','r',encoding='UTF-8') as search_file:
            student_info = search_file.readlines()
            index = 1
            self.student_query = []
            for item in student_info:
                info = dict(eval(item))
                self.student_query.append(info)
            for item in self.student_query:
                self.tree_view.insert('', index + 1, values=(
                    item['id'], item['姓名'], item['语文'], item['数学'], item['英语'], (int(item['语文']) + int(item['数学']) + int(item['英语']))
                ))
        tk.Button(self, text='刷新', command=self.show_content2).pack()

    def show_content2(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        with open('student.txt','r',encoding='UTF-8') as search_file:
            student_info = search_file.readlines()
            index = 1
            self.student_query = []
            for item in student_info:
                info = dict(eval(item))
                self.student_query.append(info)
            for item in self.student_query:
                self.tree_view.insert('', index + 1, values=(
                    item['id'], item['姓名'], item['语文'], item['数学'], item['英语'], (int(item['语文']) + int(item['数学']) + int(item['英语']))
                ))

    def tree_view_sort_column(self, col,reverse):
        l = [(self.tree_view.set(k, col), k) for k in self.tree_view.get_children('')]
        l.sort(key=lambda t: int(t[0]),reverse=reverse)
        for index, (val, k) in enumerate(l):
            self.tree_view.move(k, '', index)
        self.tree_view.heading(col, command=lambda: self.tree_view_sort_column(col,False))