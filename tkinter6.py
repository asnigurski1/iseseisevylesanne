#Artur Snigurski
#IT20
#Ülesanne 6

from tkinter import *
import time

aken = Tk()
aken.title('Taani')
aken.iconbitmap('gang1.ico')

#lõuendi loomine
louend = Canvas(aken, width=2000, height=2000)
louend.pack()

#Taani lipp
louend.create_rectangle(100, 20, 300, 150, fill='#C60C30', outline='#C60C30')
louend.create_rectangle(170, 20, 195, 150, fill='white', outline='white')
louend.create_rectangle(100, 70, 300, 100, fill='white', outline='white')

minu_pilt = PhotoImage(file='naine.png')
louend.create_image(100, 200, anchor=NW, image=minu_pilt)


aken.mainloop()