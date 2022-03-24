from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400+500+250")
backgroundColor = Label(bg="#708090", width=400, height=400)
backgroundColor.place(x=0, y=0)
root.resizable(width=False, height=False)   

v = StringVar(value=0)
v2 = StringVar(value=0)
s = 55
y = 30
acikMavi = "#00FFFF"

def clear():
    sonuc["text"]="Sonuç : 0"

def topla():
    toplaSonuc = int(entry1.get()) + int(entry2.get())
    sonuc["text"]="Sonuç : {0}".format(toplaSonuc)

def cikar():
    cikarSonuc = int(entry1.get()) - int(entry2.get())
    sonuc["text"]="Sonuç : {0}".format(cikarSonuc)

def carp():
    carpSonuc = int(entry1.get()) * int(entry2.get())
    sonuc["text"]="Sonuç : {0}".format(carpSonuc)

def bol():
    bolSonuc = int(entry1.get()) / int(entry2.get())
    sonuc["text"]="Sonuç : {0}".format(bolSonuc)

entry1 = Entry(bg="#008B8B", font="Arial 26", justify="right", textvariable=v)
entry1.place(x=10, y=10)

entry2 = Entry(bg="#008B8B", font="Arial 26", justify="right", textvariable=v2)
entry2.place(x=10, y=60)

sonuc = Label(bg="#708090", font="Arial 24", justify="right", text="Sonuç : 0")
sonuc.place(x=10, y=350)

toplama = Button(text="+",width=2,font="Arial 24", bg=acikMavi, fg="black", command=topla)
toplama.place(x=80+s, y=180-y)

cikarma = Button(text="-", width=2,font="Arial 24", bg=acikMavi, fg="black", command=cikar)
cikarma.place(x=180+s, y=180-y)

carpma = Button(text="x",width=2,font="Arial 24", bg=acikMavi, fg="black", command=carp)
carpma.place(x=80+s, y=250-y)

bolme = Button(text="/", width=2,font="Arial 24", bg=acikMavi, fg="black", command=bol)
bolme.place(x=180+s, y=250-y)

sil = Button(text="c",width=2,font="Arial 24", bg=acikMavi, fg="black", command=clear)
sil.place(x=350, y=110)

root.mainloop()
