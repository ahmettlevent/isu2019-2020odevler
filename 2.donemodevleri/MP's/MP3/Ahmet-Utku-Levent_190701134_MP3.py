import tkinter as tk
from tkinter import *
from tkinter import filedialog, Label, messagebox


class Kumeleme(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.excelFile_path=str()
        self.radiosecimi = IntVar()

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.inituI()
        self.ListboxYukle()

    def inituI(self):
        Label(self.parent, bg="red").place(x=0, y=25, width=2000, height=5)
        Label(self.parent, bg="red").place(x=0, y=500, width=2000, height=5)
        Label(self.parent, bg="misty rose", text="EYALET KÜMELEME").place(x=245, y=15, width=320, height=25)
        Label(self.parent, text='KÜMELEME METODU', bg="misty rose").place(x=485, y=155, width=210, height=25)
        Label(self.parent, bg="misty rose", text="İLK HARFİ SEÇ").place(x=55, y=140, width=217, height=25)
        Label(self.parent, bg="misty rose", text="K:").place(x=640, y=270, width=17, height=21)
        Label(self.parent, text='BİTKİ VERİ SETİNİ YÜKLE', bg="white").place(x=245, y=95, width=210, height=25)
        Button(self.parent, text="KÜMELERİ GÖSTER",command=self.TextWidget).place(x=300, y=365, width=170, height=25)
        Button(self.parent, text='ARA', command=self.ara).place(x=490, y=95)
        self.mylist = Listbox(self.parent,selectmode='multiple')
        self.mylist.place(x=65, y=185, width=180, height=85)
        self.scrollbarekle(self.mylist)
        Entry(self.parent, ).place(x=675, y=270, width=40, height=20)

        self.T = Text(self.parent, bg='misty rose')
        self.T.place(x=0, y=409, height=200, width=800)
        self.T.insert(tk.END, "")
        self.scrollbarekle(self.T)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="K-Means",
                    variable=self.radiosecimi, value=1).place(x=530, y=225, width=95)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Hiyerarşik",
                    variable=self.radiosecimi, value=2).place(x=530, y=265, width=95)

    def scrollbarekle(self, Listbox):
        # Listbox'a scrollbar ekleme
        scrollbar_y = Scrollbar(Listbox, width=12)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=Listbox.yview)
        Listbox.config(yscrollcommand=scrollbar_y.set)
        Listbox.config(yscrollcommand=scrollbar_y.set)

    def ara(self):
        # Excel Secimi ve Kontrol
        try:
            self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                             filetypes=(("Txt file", "*.txt"),))
        except IOError:
            messagebox.showwarning("Uyari ", "Lutfen Gecerli Bir Dosya Secin ! ")

    def ListboxYukle(self):
        for i in self.alphabet:
            self.mylist.insert(END,i)

    def TextWidget(self):
        try:
            sonuc = self.Matris()
            for i in sonuc:
                self.T.insert(END,i)
        except TclError:
            messagebox.showwarning("Hata","ListBox'tan Birsey Seciniz")
        except FileNotFoundError:
            messagebox.showwarning("Hata","Veri Dosyasini Seciniz")

    def Matris(self):
        a = tuple((self.mylist.selection_get()).split("\n"))
        dataDict = self.readfile(self.excelFile_path)
        for i in dataDict.keys():
            if i.startswith(a):
                print(dataDict[i])
        return 

    def readfile(self,filename):
      lines=[line for line in open(filename, "r").readlines()]
      rownames=[]
      data=[]
      for line in lines:
        p=line.strip().split(',')
        rownames.append(p[0])
        data.append([x for x in p[1:]])
      dataDict = dict(zip(rownames, data))
      return dataDict

def main():
    root = Tk()
    root.geometry("800x600+325+55")
    root.resizable(width=False, height=False)
    root.configure(bg="black")
    app = Kumeleme(root)
    root.mainloop()


main()
