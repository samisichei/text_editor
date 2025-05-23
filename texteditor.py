import sys

v=sys.version

if "2.7" in v:
    from Tkinter import *
    import tkinter.filedialog

elif "3.3" in v or "3.4" or "3.10" in v:
    from tkinter import *
    import tkinter.filedialog

root = Tk()
root.title("Text Editor")

text = Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
    
button = Button(root, text="save", command=saveas)
button.grid()

def FontHelvetica():
    text.config(font="Helvetica")
    
def FontCourier():
    text.config(font="Courier")

def FontArial():
    text.config(font="Arial")

def FontTimes():
    text.config(font="Times")

def bgwhite():
    text.config(bg="white")

def bgBlack():
    text.config(bg="black", fg="white")

def bgYellow():
    text.config(bg="yellow")

def bgLightBlue():
    text.config(bg="light blue", fg="black")

font = Menubutton(root, text="Font")
font.grid()

font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

helvetica = IntVar()
courier = IntVar()
arial = IntVar()
times = IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Arial", variable=arial, command=FontArial)
font.menu.add_checkbutton(label="Times", variable=times, command=FontTimes)

bgmenu = Menubutton(root, text="Background", relief=RAISED)
bgmenu.grid()

bgmenu.menu = Menu(bgmenu, tearoff=0)
bgmenu["menu"] = bgmenu.menu

white = IntVar()
black = IntVar()
yellow = IntVar()
lightblue = IntVar()

bgmenu.menu.add_checkbutton(label="White", variable=white, command=bgwhite)
bgmenu.menu.add_checkbutton(label="Black", variable=black, command=bgBlack)
bgmenu.menu.add_checkbutton(label="Yellow", variable=yellow, command=bgYellow)
bgmenu.menu.add_checkbutton(label="Light Blue", variable=lightblue, command=bgLightBlue)

root.mainloop()
