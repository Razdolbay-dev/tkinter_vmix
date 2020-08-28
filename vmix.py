# Vse cto otnositsya k Tkinter
import tkinter as tk
from tkinter import ttk
#from tkinter.ttk import Lable
# Storonnie module
import xml.etree.ElementTree as ET
import os


list_input = []
guid = ()
key = None
items = []

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        #Add button to open manager Frame
        self.add_img = tk.PhotoImage(file='res/clock.png')
        btn_open_dialog = tk.Button(toolbar, text='Добавить задачу', command=self.open_dialog,
                                    bg='gray', bd=0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)
        # Дерево
        b_frame = tk.Frame(root)
        b_frame.pack(side=tk.TOP, expand="yes", fill=tk.BOTH)
        self.tree = ttk.Treeview(b_frame, columns=('Title', 'GUID', 'Duration', 'Start', 'End'), height=15, show='headings')

        self.tree.column('Title', width=150, anchor=tk.CENTER)
        self.tree.column('GUID', width=200, anchor=tk.CENTER)
        self.tree.column('Duration', width=170, anchor=tk.CENTER)
        self.tree.column('Start', width=200, anchor=tk.CENTER)
        self.tree.column('End', width=200, anchor=tk.CENTER)

        self.tree.heading('Title',text='Input')
        self.tree.heading('GUID',text='Ключ')
        self.tree.heading('Duration',text='Проболжительность')
        self.tree.heading('Start',text='Начало')
        self.tree.heading('End',text='Конец')
        self.tree.pack(side=tk.LEFT, expand="yes", fill=tk.BOTH)

    def records(self, title, guid, duration, start, end):
        pass

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        #list_input = []
        #guid = ()
        #key = None
        #items = []
        pars(list_input)
        self.init_child()

    def init_child(self):
        items = []
        key = 'NONE'
        for t in list_input:
            title = t['Title']
            items.append(title)
        self.title("Добавить задачу")
        self.geometry('800x600+300+200')
        self.resizable(False, False)

        lbl_title = tk.Label(self, text='Имя')
        lbl_title.place(x=50, y=50)
        #self.entry_title = ttk.Entry(self)
        #self.entry_title.place(x=200, y=50)
        lbl_test = tk.Label(self, text='')
        lbl_test.place(x=50, y=380)

        lbl_title = tk.Label(self, text='GUID')
        lbl_title.place(x=50, y=100)
        self.entry_guid = ttk.Entry(self)
        self.entry_guid.place(x=200, y=100)

        lbl_duration = tk.Label(self, text='Продолжительность')
        lbl_duration.place(x=50, y=150)
        self.entry_duration = ttk.Entry(self)
        self.entry_duration.place(x=200, y=150)
        self.v = tk.StringVar("1123321")
        lbl_start = tk.Label(self, text='Начало')
        lbl_start.place(x=50, y=200)
        self.entry_start = ttk.Entry(self)
        self.entry_start.place(x=200, y=200)
        lbl_end = tk.Label(self, text='Конец')
        lbl_end.place(x=50, y=250)
        self.entry_end = ttk.Entry(self, text='')
        self.entry_end.insert = (0, v)
        self.entry_end.place(x=200, y=250)

        btn_close = ttk.Button(self, text='close', command=self.destroy)
        btn_close.place(x=320, y=300)
        btn_add = ttk.Button(self, text='Add', command=self.edit_entry)
        btn_add.place(x=220, y=300)
        btn_add.bind()
        btn_pars = ttk.Button(self, text='Parsing', command=self.change)
        btn_pars.place(x=120, y=300)
        btn_pars.bind()
        self.combobox = ttk.Combobox(self, values=list(items))
        self.combobox.current(0)
        self.combobox.place(x=200, y=50)
        #Удерживает фокус на окне. До выполнения задачи не может взаимодействовать с основным окном
        self.grab_set()
        self.focus_set()

    def edit_entry(self, ):
        name = self.combobox.get()
        for i in list_input:
            title = i['Title']
            if title == name:
                key = i['GUID']
                return key
                
def change(key):
    name = combobox.get()
    for i in list_input:
        title = i['Title']
        if title == name:
            key = i['GUID']
            return key

def get_items(title):
    for t in list_input:
        title = t['Title']
        items.append(title)

def pars(value):
    os.system('curl -o vmix.xml http://10.1.0.8:8088/API')
    root = ET.parse('vmix.xml').getroot()
    root_find = root.findall('inputs/')
    for tag in root_find:
        title = tag.get('title')
        key = tag.get('key')
        duration = tag.get('duration')
        input = tag.get('number')
        data = {'Input': input,'Title': title, 'GUID': key, 'Time': duration}
        list_input.append(data)

def clicked():
#    result = pars(list_input)
    guid = change(key)
    lbl.configure(text=guid)

def get_list_inputs():
    list_input.clear()

    result = pars(list_input)
    combo['values'] = (list_input)

def clear_list():
    list_input.clear()
    items.clear()
    result = pars(list_input)
    get_items(items)
    combo['values'] = (items)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Добро пожаловать vMixSheduler")
    #root.geometry('650x450+300+200')
    #root.resizable(False, False)
    #combo = Combobox(root)
    #combo['values'] = (list_input)
    #combo.current(list_input['input'])  # установите вариант по умолчанию
    #combo.grid(column=0, row=1)
    #lbl = Label(root, text="Привет")
    #lbl.grid(column=0, row=0)
    #txt = Entry(root,width=10)
    #txt.grid(column=1, row=0)
    #btn1 = Button(root, text="GUID", command=clicked)
    #btn1.grid(column=2, row=2)
    #btn2 = Button(root, text="Update Info", command=get_list_inputs)
    #btn2.grid(column=2, row=0)
    #btn3 = Button(root, text="Update List", command=clear_list)
    #btn3.grid(column=2, row=1)
    root.mainloop()
