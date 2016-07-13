from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo,showwarning,showerror

root=Tk()
root.title("Text Editor")
texteditor=ScrolledText(root,height=100,width=800)
def file_new():
    return

def file_open():
    a=messagebox.askyesno(title="GUARRENTY",message="Are You Sure To Open The File")
    showinfo("INFO","Retrive from location where you saved")
    if a==True:
        open_file=filedialog.askopenfile(parent=root,mode='rb',title="SELECT FILE TO BE OPENED")
    if open_file!=None:
        contents=open_file.read()
        texteditor.insert('1.0',contents)
        open_file.close()

def file_save():
    showinfo("INFO","Remember Location Where You Are Saving Your File")
    if messagebox.askokcancel(title="SAVING LOCATION",message="Enter Location Where You Have To Save The File"):
       save_file=filedialog.asksaveasfile(mode='w')
    if save_file!=None:
        data=texteditor.get('1.0',END+'-1c')
        save_file.write(data)
        save_file.close()

def message_exit():
    showwarning("WARNING","You Are Going To Exit")
    if messagebox.askyesno(title="SURITY",message="Are You Sure TO Exit This Is Your Life"):
        root.destroy()

def message_about():
    showinfo("PRINCE ENTERPRISES","PRINCE SATYA PRAKASH")
    return

def message_help():
    return

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="New",command=file_new)
filemenu.add_command(label="Open",command=file_open)
filemenu.add_command(label="Save",command=file_save)
filemenu.add_command(label="Exit",command=message_exit)

menubar.add_cascade(label="File",menu=filemenu)
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=message_about)
helpmenu.add_command(label="Help",command=message_about)
menubar.add_cascade(label="Help",menu=helpmenu)

texteditor.pack()
root.config(menu=menubar)
root.mainloop()

