#Artur Snigurski
#IT20
#Ülesanne 3

from tkinter import *

aken = Tk()
aken.title('Artur Snigurski')
aken.configure(background='black')
aken.iconbitmap('gang1.ico')
aken.resizable(0, 0)



Label(aken, text='Artur Snigurski \nIT20\n2021', foreground="red", background="black", pady=10, padx=30, font="Tahoma 16 bold italic").pack()


aken.mainloop()

