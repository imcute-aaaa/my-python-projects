from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os


root = Tk()
root.title('记事本')


root.geometry("800x500+100+100")

filename = ''


def author():

    tkinter.messagebox.askokcancel()


def about():

    tkinter.messagebox.askokcancel('版权信息.Copyright', '随意转载啦!')

# 定义文件子菜单对应的相关函数


def openfile():
    global filename
    filename = tkinter.filedialog.askopenfilename(defaultextension='.txt')

    if filename == '':
        filename = None
    else:
        root.title('FileName:'+os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r', encoding='utf-8')  # 注意后面要加上读取的编码格式，否则报编码错误
        textPad.insert(1.0, f.read())
        f.close()


def new():
    global filename
    root.title("未命名文件")
    filename = None
    textPad.delete(1.0, END)


def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()
filename=''

def saveas():
    f = tkinter.filedialog.asksaveasfilename(initialfile='blank.txt', defaultextension='.txt')
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


def search():
    topsearch = Toplevel(root)
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找')
    button1.grid(row=0, column=2)


menubar = Menu(root)
root.config(menu=menubar)


filemenu = Menu(menubar)

filemenu.add_command(label='新建', accelerator='Ctrl+N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl+O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl+S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)


editmenu = Menu(menubar)
editmenu.add_command(label='撤消', accelerator='Ctrl+z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl+y', command=redo)
# 添加分割线
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl+X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl+C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl+V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl+F', command=search)
editmenu.add_command(label='全选', accelerator='Ctrl+A', command=selectAll)
menubar.add_cascade(label='编辑', menu=editmenu)


aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu=aboutmenu)


toolbar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toolbar, text='打开', command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='保存', command=save)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO, fill=X)


status = Label(root, text="Ln20", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()
