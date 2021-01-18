#Artur Snigurski
#IT20
#Ülesanne 5


from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.iconbitmap('gang1.ico')
aken.geometry("300x300")

#funktsioonid
def kaibemaks():
    summa = float(sisestus.get())
    km = float(var.get())
    km_kokku = summa / 100 * km
    km_kokku1 = summa + km_kokku
    vastus4.config(text=km_kokku)
    vastus5.config(text=km_kokku1)
  
#silt
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)


#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

def naita_valikut():
    pass
    #print(var.get())

#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=naita_valikut)
valikukast.grid(row=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20, command=naita_valikut)
valikukast.grid(row=2)

#nupud
nupp1 = Button(aken, text="OK", width=10, command=kaibemaks)
nupp1.grid(row=1, column=1)

#silt2
vastus = Label(aken, text="Käibemaks :")
vastus.grid(row=3,column=0)

#silt3
vastus3 = Label(aken, text="Hind käibemaksuga :")
vastus3.grid(row=4,column=0)

#silt4
vastus4 = Label(aken, text="0.00€")
vastus4.grid(row=3, column=1)

#silt5
vastus5 = Label(aken, text="0.00€")
vastus5.grid(row=4, column=1)


aken.mainloop()
