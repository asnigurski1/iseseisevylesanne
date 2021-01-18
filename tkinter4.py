#Artur Snigurski
#IT20
#Ülesanne 4


from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack()


root.title('Artur Snigurski')
root.iconbitmap('gang1.ico')
root.geometry("200x200")
root.resizable(0, 0)
root.option_add('*font', ('tahoma', 12))


#lorem = 'Siia kunagi tekst'
#tekst = Label(aken, text=lorem, justify=CENTER, font="Tahoma 12")
#tekst.pack()


nupp1 = Button(frame, root, text="1")
nupp1.pack(side=LEFT, fill = X, expand=YES, pady=2, padx=2)
nupp2 = Button(frame, root, text="2")
nupp2.pack(side=LEFT, fill = X, expand=YES, pady=2, padx=2)
nupp3 = Button(frame, root, text="3")
nupp3.pack(side=LEFT, fill = X, expand=YES, pady=2, padx=2)
nupp4 = Button(frame, root, text="/")
nupp4.pack(side=LEFT, fill = X, expand=YES, pady=2, padx=2)
nupp5 = Button(frame, root, text="4")
nupp5.pack(side=TOP, expand=YES, pady=2, padx=2)
aken.mainloop()


