from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title("Green Notpad (Created by KNOT)")
root.config(bg="green4")
root.resizable(False,False)

def save_file():
    open_file = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
    if open_file is None :
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode = "r", filetypes = [("Text Files","*.txt")])
    if file is not None :
        content = file.read()
    entry.insert(INSERT,content)


entry = Text(root,height = "33",width = "72",wrap = WORD)
entry.place(x = 10,y = 10)

button1 = Button(root,width = "26",height = "2",bg = "#fff",text = "Save your file",command = save_file).place(x = 100,y = 550)
button2 = Button(root,width = "26",height = "2",bg = "#fff",text = "Open your file",command = open_file).place(x = 300,y = 550)

root.mainloop()
