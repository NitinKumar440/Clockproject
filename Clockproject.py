from tkinter import *
from time import strftime



def tym():
    t= strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    #displays the time
    lbl.after(1000,tym)




lbl = Label(clock, font = ('calibri', 40, 'bold'),
background = 'yellowgreen',
foreground = 'white')




lbl.pack(anchor = 'centre')
time()



mainloop()