import tkinter
from info import generalInfo
from statisticsPage import statisticsPage

def about():
    tkinter.messagebox.showinfo("Diabetic Predictor","Done by Nermeen Zaki $ Menna Yasser")

def mainMenue(x):
    menu = tkinter.Menu(x)
    x.config(menu=menu)
    subm1 = tkinter.Menu(menu)
    menu.add_cascade(label='File', menu=subm1)
    subm1.add_command(label='Exit', command=x.destroy)

    subm2 = tkinter.Menu(menu)
    menu.add_cascade(label='Information', menu=subm2)
    subm2.add_command(label='Info', command=generalInfo)
    subm2.add_command(label='Statistics', command=statisticsPage)

    menu.add_cascade(label='About', command=about)