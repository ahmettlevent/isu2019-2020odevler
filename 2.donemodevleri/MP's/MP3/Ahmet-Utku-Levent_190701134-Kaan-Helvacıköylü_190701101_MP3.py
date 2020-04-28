import tkinter as tk
from tkinter import *
from tkinter import filedialog, Label, messagebox

from clusters import *


class Kumeleme(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.kdegeri= IntVar()
        self.stateNamesShort = {}
        self.excelFile_path = str()
        self.radiosecimi = IntVar()
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.extractStateList()
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
        Button(self.parent, text="KÜMELERİ GÖSTER", command=self.TextWidget).place(x=300, y=365, width=170, height=25)
        Button(self.parent, text='ARA', command=self.ara).place(x=490, y=95)
        self.mylist = Listbox(self.parent, selectmode='multiple')
        self.mylist.place(x=65, y=185, width=180, height=85)
        self.scrollbarekle(self.mylist)
        Entry(self.parent,textvariable=self.kdegeri).place(x=675, y=270, width=40, height=20)

        self.T = tk.Text(self.parent, bg='misty rose',relief =SUNKEN)
        self.T.place(x=0, y=390, height=200, width=800)
        self.scrollbarekle(self.T)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Hiyerarşik",
                    variable=self.radiosecimi, value=1).place(x=530, y=225, width=95)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="K-Means",
                    variable=self.radiosecimi, value=2).place(x=530, y=265, width=95)

    def scrollbarekle(self, Listbox):
        # Listbox'a scrollbar ekleme
        scrollbar_y = Scrollbar(Listbox, width=12)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=Listbox.yview)
        Listbox.config(yscrollcommand=scrollbar_y.set)

        scrollbar_x = Scrollbar(Listbox, orient='horizontal',width=11)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=Listbox.xview)
        Listbox.config(xscrollcommand=scrollbar_x.set)


    def ara(self):
        # Excel Secimi ve Kontrol
        try:
            self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                             filetypes=(("Txt file", "*.txt"),))
        except IOError:
            messagebox.showwarning("Uyari ", "Lutfen Gecerli Bir Dosya Secin ! ")

    def ListboxYukle(self):
        for i in self.alphabet:
            self.mylist.insert(END, i)

    def TextWidget(self):
        try:
            self.Matris()
            if self.radiosecimi.get() == 1:
                self.hierarchkumele()
            elif self.radiosecimi.get() == 2:
                print(self.kdegeri.get())
                self.k_means_kumeleme()
        except TclError:
            messagebox.showwarning("Hata", "ListBox'tan Birsey Seciniz")
        except FileNotFoundError:
            messagebox.showwarning("Hata", "Veri Dosyasini Seciniz")

    def Matris(self):
        with open("190701134_data.txt", "w", encoding="utf-8") as matris_file:
            a = tuple((self.mylist.selection_get()).split("\n"))
            dataDict = self.dataExtractFile(self.excelFile_path)
            for i in dataDict.keys():
                matris_file.writelines(i+",")
            matris_file.writelines("\n")
            for i in self.stateNamesShort:
                matris_file.writelines(i)
                for j in dataDict.values():
                    if i in j:
                        matris_file.writelines(","+"1")
                    else: matris_file.writelines(","+"0")
                matris_file.writelines("\n")

    def dataExtractFile(self, filename):
        lines = [line for line in open(filename, "r").readlines()]
        rownames = []
        data = []
        for line in lines:
            p = line.strip().split(',')
            rownames.append(p[0])
            data.append([x for x in p[1:]])
        dataDict = dict(zip(rownames, data))
        return dataDict

    def extractStateList(self):
        with open("stateabbr.txt", "r") as states:
            for i in states.readlines()[2:100]:
                word_list = i.split(None, 1)
                self.stateNamesShort[word_list[0]] = (word_list[1][:-1]).replace('\t','')
            self.stateNamesShort.pop("Prince")

    # K-Means KÜMELE
    def k_means_kumeleme(self):
        (self.citys, plants, data) = self.readfile_New("190701134_data.txt")
        kclust = kcluster(rows=data,distance=tanamoto,k=self.kdegeri.get())
        for i in range(self.kdegeri.get()):
            print([self.citys[r] for r in kclust[i]])



    # HİYERARŞİK KÜMELE
    def hierarchkumele(self):
        (self.citys, plants, data) = self.readfile_New("190701134_data.txt")
        hclust = hcluster(data)
        self.printclust_new(clust=hclust)

    def printclust_new(self, clust, labels=None, n=0):
        # indent to make a hierarchy layout
        for i in range(n): self.T.insert(END, ' ')
        if clust.id < 0:
            # negative id means that this is branch
            self.T.insert(END, '-\n')
        else:

            if labels == None:
                self.T.insert(END, self.stateNamesShort[self.citys[clust.id]] + "\n")
            else:
                self.T.insert(END, labels[self.stateNamesShort[self.citys[clust.id]]] + "\n")

        if clust.left != None: self.printclust_new(clust.left, labels=labels, n=n + 1)
        if clust.right != None: self.printclust_new(clust.right, labels=labels, n=n + 1)

    def readfile_New(self, filename):
        lines = [line for line in open(filename, "r").readlines()]
        # First line is the column titles
        colnames = lines[0].strip().split(',')
        rownames = []
        data = []
        for line in lines[1:]:
            p = line.strip().split(',')
            # First column in each row is the rowname
            rownames.append(p[0])
            # The data for this row is the remainder of the row
            data.append([float(x) for x in p[1:]])
        return rownames, colnames[:-1], data


def main():
    root = Tk()
    root.geometry("800x600+325+55")
    root.resizable(width=False, height=False)
    root.configure(bg="black")
    app = Kumeleme(root)
    root.mainloop()

main()
