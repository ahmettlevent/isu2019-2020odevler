import os
from tkinter import *
from tkinter import IntVar


class Analiz(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.siralama_var = IntVar()
        self.call()
        # self.initUI()
        # self.initUI_Data()

    def initUI(self):
        # Programın arayüzünü oluşturduk
        Label(self.parent, bg="misty rose", text="Dosya Arayıcı", width=70).grid(row=0, column=1, pady=10, ipadx=10,
                                                                                 ipady=10, columnspan=3)

        Label(self.parent, bg="misty rose", text="Başlangıç Dizini").grid(row=1, column=0, padx=0, pady=15)

        Text(self.parent, width=55, height=1.2).grid(row=1, column=1, ipadx=0, pady=5, columnspan=2)

        Label(self.parent, bg="misty rose", text="Derinlik").grid(row=2, column=1, padx=20, ipady=0)

        Entry(self.parent, width=10).grid(row=2, column=1, padx=0, ipady=0, columnspan=3)

        Button(self.parent, bg="misty rose", text="Index Oluştur").grid(row=2, column=2, padx=0, ipady=0, pady=20)

        Text(self.parent, width=25, height=1.2).grid(row=3, column=1, ipadx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Sıralama Krıteri").grid(row=4, column=1, padx=0, pady=15)

        Label(self.parent, bg="misty rose", text="Ağırlıklar").grid(row=4, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3).grid(row=5, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3).grid(row=6, columnspan=15, padx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Filtre").grid(row=4, column=3, padx=0, ipady=0)

        self.filtre = Listbox(self.parent, bg="misty rose", width=21, height=2)
        self.filtre.grid(row=5, column=3, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Ara").grid(row=5, column=4, padx=0, ipady=0, pady=0)

        Listbox(self.parent, bg="misty rose", width=81, height=15).grid(row=7, column=1, padx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Sayfa").grid(row=8, column=1, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Önceki").grid(row=8, column=1, padx=50, ipady=0, pady=0,
                                                                 columnspan=3)

        Label(self.parent, bg="misty rose", text="", width=3, height=1).grid(row=8, column=2, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Sonraki").grid(row=8, column=3, padx=0, ipady=0, pady=0,
                                                                  columnspan=3)

        R1 = Radiobutton(self.parent, text="Kelime Uzaklığı", variable=self.siralama_var, value=0, command="")
        R1.grid(row=5, column=1)

        R2 = Radiobutton(self.parent, text="Erişim Zamanı", variable=self.siralama_var, value=1, command="")
        R2.grid(row=6, column=1, pady=20)

    def call(self):
        self.Search("C:\Program Files",2)

    def initUI_Data(self):
        self.filtre.configure(selectmode=MULTIPLE)
        self.filtre.insert(END, "Düz Metin")
        self.filtre.insert(END, "Program Kodu")

    def Search(self,startdirectory,depth):
        fileList = {}
        depth = 4
        startdirectory = os.path.abspath(os.path.expanduser(os.path.expandvars(startdirectory)))

        for root, dirs, files in os.walk(startdirectory):
            if root[len(startdirectory):].count(os.sep) < depth:
                for f in files:
                    item = os.path.join(root, f)
                    fileList[item] = []
        return fileList

# Programın çalışması için gerekli fonksiyonu yazdık
def main():
    root = Tk()
    root.geometry("1000x800+280+25")
    root.resizable(width=FALSE, height=FALSE)
    root.configure(bg="darkslategrey")
    app = Analiz(root)
    # root.mainloop()


main()
