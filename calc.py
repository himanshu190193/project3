#### Clculator coding#########
from tkinter import*
root = Tk()

root.geometry('1200x1000')
root.title('Welcome again')
root.config(bg='powder blue')

def click(event):
    text = event.widget.cget('text')
    print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())

        scvalue.set(value)
        screen.update()
    elif text=='c':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


f1 = Frame(root, bd=10, bg='grey', relief=GROOVE, borderwidth=10)
f1.place(x=300, y=20, width=436, height=535)
scvalue = StringVar()
scvalue.set("")
screen = Entry(f1,textvar=scvalue, font='lucida 55 bold', bg='white')
screen.pack(side=TOP)

f2 = Frame(f1, bg='white')
b1 = Button(f2, text='9', font='lucida 20 bold',bd=7, relief=RAISED, height=1, width=7)
b1.bind("<Button-1>", click)
b1.grid(row=0, column=0)
b2 = Button(f2, text='8', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f2, text='7', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f2.place(x=0, y=100, width=416, height=65)

f3 = Frame(f1, bg='white')
b1 = Button(f3, text='6', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b1.bind('<Button-1>', click)
b1.grid(row=0, column=0)
b2 = Button(f3, text='5', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f3, text='4', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f3.place(x=0, y=170, width=416, height=65)

f4 = Frame(f1, bg='white')
b1 = Button(f4, text='3', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b1.bind('<Button-1>', click)
b1.grid(row=0, column=0)
b2 = Button(f4, text='2', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f4, text='1', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f4.place(x=0, y=240, width=416, height=65)

f5 = Frame(f1, bg='white')
b1 = Button(f5, text='+', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b1.bind('<Button-1>', click)
b1.grid(row=0, column=0)
b2 = Button(f5, text='0', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f5, text='-', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f5.place(x=0, y=310, width=416, height=65)

f6 = Frame(f1, bg='white')
b1 = Button(f6, text='*', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b1.bind('<Button-1>', click)
b1.grid(row=0, column=0)
b2 = Button(f6, text='%', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f6, text='/', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f6.place(x=0, y=380, width=416, height=65)

f7 = Frame(f1, bg='white')
b1 = Button(f7, text='c', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b1.bind('<Button-1>', click)
b1.grid(row=0, column=0)
b2 = Button(f7, text='.', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b2.bind('<Button-1>', click)
b2.grid(row=0, column=1)
b3 = Button(f7, text='=', font='lucida 20 bold', bd=7, relief=RAISED, height=1, width=7)
b3.bind('<Button-1>', click)
b3.grid(row=0, column=2)
f7.place(x=0, y=450, width=416, height=65)



root.mainloop()