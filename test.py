from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()

f1 = Frame(root)
f2 = Frame(root)

f1.pack(fill=BOTH, expand="yes", side=TOP)
f2.pack(fill=BOTH, expand="yes", side=TOP)

tree = ttk.Treeview(f2, columns=('Title', 'GUID', 'Duration', 'Start', 'End'), height=10, show='headings')
tree.pack()

tree.heading('Title',text='Имя Input')
tree.heading('GUID',text='Ключ')
tree.heading('Duration',text='Проболжительность')
tree.heading('Start',text='Начало')
tree.heading('End',text='Конец')
 

root.title("Добро пожаловать vMixSheduler")
#root.geometry('650x450+300+200')
root.mainloop()