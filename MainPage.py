#!/usr/bin/python
# -*- coding:UTF-8 -*-

import tkinter as tk
from view import AboutFrame, ModifyFrame, InsertFrame, SearchFrame, DeleteFrame, TotalFrame, ContentFrame


# 主页
class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('学生信息管理系统')
        self.root.geometry('600x400')
        self.create_page()
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.modify_frame = ModifyFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.about_frame = AboutFrame(self.root)
        self.total_frame = TotalFrame(self.root)
        self.content_frame = ContentFrame(self.root)

    def create_page(self):
        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入', command=self.show_insert)
        menubar.add_command(label='查询', command=self.show_search)
        menubar.add_command(label='修改', command=self.show_modify)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='统计', command=self.show_total)
        menubar.add_command(label='概览', command=self.show_content)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.total_frame.pack_forget()
        self.content_frame.pack_forget()

    def show_insert(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.total_frame.pack_forget()
        self.content_frame.pack_forget()
        pass

    def show_search(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack()
        self.delete_frame.pack_forget()
        self.total_frame.pack_forget()
        self.content_frame.pack_forget()
        pass

    def show_delete(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack()
        self.total_frame.pack_forget()
        self.content_frame.pack_forget()
        pass

    def show_modify(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.total_frame.pack_forget()
        self.content_frame.pack_forget()
        pass

    def show_total(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.total_frame.pack()
        self.content_frame.pack_forget()
        pass

    def show_content(self):
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.total_frame.pack_forget()
        self.content_frame.pack()
        pass
