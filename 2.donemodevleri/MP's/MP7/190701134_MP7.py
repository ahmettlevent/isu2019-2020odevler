import os
import shelve
import time
from tkinter import *
from tkinter import messagebox
import re

# WORD CHECK Decorator --
def wordCheck(func):
    '''
    Bu Decorator'un iki farkli islevi bulunmaktadir
    Kelime uzakligi kriteri icin:
            Kelime uzakliklarini hesaplar ve yeni bir liste dondurur.Kelimeleri kontrol eder.
    Zaman kriteri icin:
            Kelime uzakliklarini hesaplar fakat bunun sonuca faydası olmayacağından ,
            bu kriter için faydası sadece kelimeleri kontrol etmek olacaktır.
    '''
    def wrapper(self, searchDB, agirlik=1):
        # stackoverflow'dan re örneği alınmıştır. https://stackoverflow.com/questions/7881794/dont-split-double-quoted-words-with-python-string-split

        entry = self.userwords.get()
        wordlist = re.findall(r'(\w+|".*?")', entry)
        if len(wordlist) == 0:
            messagebox.showerror("HATA","Lütfen En Az Bir Kelime Giriniz")
        else:
            wordDB = {}
            for path in searchDB:
                content = (searchDB[path]["content"]).strip().split(' ')
                counter = 0
                score = 0
                word_is_in=[]
                for word in content:
                    try:
                        if word == wordlist[counter]:
                            word_is_in.append(word)
                            counter += 1
                        elif word != wordlist[counter] and counter>0:
                            score += 1
                    except IndexError:
                        break
                if wordlist == word_is_in :
                    searchDB[path]["score"] = score
                    wordDB[path] = searchDB[path]
            func(self, wordDB, agirlik=1)

    return wrapper

# Time Calculate Decorator --
def calculatetime(func):
    def wrapper(*args):
        starttime = time.time()
        func(*args)
        endtime = time.time()
        result = endtime-starttime
    return wrapper
# -------------------------

class Analiz(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.k_uzaklik = BooleanVar()
        self.e_zaman = BooleanVar()

        self.startdir = StringVar()
        self.startdir.set(r"C:\Users\utkul\Desktop\New folder")

        self.derinlik = StringVar()
        self.userwords= StringVar()

        self.file_paths = []

        self.initUI()

    def initUI(self):
        # Programın arayüzünü oluşturduk
        Label(self.parent, bg="misty rose", text="Dosya Arayıcı", width=70).grid(row=0, column=1, pady=10, ipadx=10,
                                                                                 ipady=10, columnspan=3)

        Label(self.parent, bg="misty rose", text="Başlangıç Dizini").grid(row=1, column=0, padx=0, pady=15)

        Entry(self.parent, width=55, textvariable=self.startdir).grid(row=1, column=1, ipadx=0, pady=5, columnspan=2)

        Label(self.parent, bg="misty rose", text="Derinlik").grid(row=2, column=1, padx=20, ipady=0)

        Entry(self.parent, width=10, textvariable=self.derinlik).grid(row=2, column=1, padx=0, ipady=0, columnspan=3)

        Button(self.parent, bg="misty rose", text="Index Oluştur", command=self.index_create).grid(row=2, column=2,
                                                                                                   padx=0,
                                                                                                   ipady=0, pady=20)

        Label(self.parent, width=10, text="Kelimeler", height=1).grid(row=3, column=0, ipadx=5, ipady=0)
        Entry(self.parent, width=25,textvariable=self.userwords).grid(row=3, column=1, ipadx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Sıralama Krıteri").grid(row=4, column=1, padx=0, pady=15)

        Label(self.parent, bg="misty rose", text="Ağırlıklar").grid(row=4, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3).grid(row=5, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3).grid(row=6, columnspan=15, padx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Filtre").grid(row=4, column=3, padx=0, ipady=0)

        self.filtre = Listbox(self.parent, bg="misty rose", width=21, height=2)
        self.filtre.grid(row=5, column=3, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", command=self.searchWords, text="Ara").grid(row=5, column=4, padx=0,
                                                                                        ipady=0,
                                                                                        pady=0)

        Listbox(self.parent, bg="misty rose", width=81, height=15).grid(row=7, column=1, padx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Sayfa").grid(row=8, column=1, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Önceki").grid(row=8, column=1, padx=50, ipady=0, pady=0,
                                                                 columnspan=3)

        Label(self.parent, bg="misty rose", text="", width=3, height=1).grid(row=8, column=2, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Sonraki").grid(row=8, column=3, padx=0, ipady=0, pady=0,
                                                                  columnspan=3)

        self.R1 = Checkbutton(self.parent, text="Kelime Uzaklığı", variable=self.k_uzaklik)
        self.R1.grid(row=5, column=1)

        self.R2 = Checkbutton(self.parent, text="Erişim Zamanı", variable=self.e_zaman)
        self.R2.grid(row=6, column=1, pady=20)

        self.filtre.configure(selectmode=MULTIPLE)
        self.filtre.insert(END, "Duz Metin")
        self.filtre.insert(END, "Program Kodu")

    def index_create(self):
        if os.path.isdir(self.startdir.get()):
            fileDic = self.FileSearch(self.startdir.get(), depth=3)
            self.index_it(fileDic)
        else:
            messagebox.showerror("ERROR !", "LUTFEN GECERLI BIR DIZIN GIRIN")

    def index_it(self, fileDic):
        db = shelve.open("veriler")
        for i in fileDic:
            db[i] = {"filedir": fileDic[i]["filedir"], "score": 0, "fileType": fileDic[i]["filetype"],
                     "content": open(i).read(), "m_time": os.stat(i).st_atime_ns}
        db.close()

    def searchWords(self):
        db = shelve.open("veriler")
        searchDB = {}
        try:
            for i in db:
                if db[i]["fileType"] in self.filtre.selection_get().split("\n"):
                    searchDB[i] = db[i]

            if self.k_uzaklik.get() == True:
                self.cook_data_k_uzaklik(searchDB, agirlik=1)
            if self.e_zaman.get() == True:
                self.cook_data_e_zaman(searchDB, agirlik=1)
            if self.k_uzaklik.get() == False and self.e_zaman.get() == False:
                messagebox.showerror("Kriter", "Lütfen bir siralama kriteri seciniz")

        except TclError:
            messagebox.showerror("Hata !", "Lütfen bir filtre seçiniz")

    @wordCheck
    def cook_data_k_uzaklik(self, searchDB, agirlik=1):
        uzakliklar = {"max":0.000000001,"min":0}
        tum_uzakliklar = []

        for i in searchDB:
            tum_uzakliklar.append(searchDB[i]["score"])

            if searchDB[i]["score"] == max(tum_uzakliklar):
                uzakliklar["max"] = searchDB[i]["score"]
            elif searchDB[i]["m_time"] == min(tum_uzakliklar):
                uzakliklar["min"] = searchDB[i]["score"]
        for i in searchDB:
            try:
                searchDB[i]["score"] = (searchDB[i]["score"] - uzakliklar["min"]) / (uzakliklar["max"] - uzakliklar["min"])
                searchDB[i]["score"] = searchDB[i]["score"]*agirlik
            except ZeroDivisionError:
                searchDB[i]["score"] = 0
    @wordCheck
    def cook_data_e_zaman(self, searchDB, agirlik=1):
        zamanlar = {"max": 0.1, "min": 0}
        tum_zamanlar = []
        for i in searchDB:
            tum_zamanlar.append(searchDB[i]["m_time"])

            if searchDB[i]["m_time"] == max(tum_zamanlar):
                zamanlar["max"] = searchDB[i]["m_time"]
            elif searchDB[i]["m_time"] == min(tum_zamanlar):
                zamanlar["min"] = searchDB[i]["m_time"]

        for i in searchDB:
            try:
                searchDB[i]["score"] = (searchDB[i]["m_time"] - zamanlar["min"]) / (zamanlar["max"] - zamanlar["min"])
                searchDB[i]["score"] = searchDB[i]["score"]
            except ZeroDivisionError:
                searchDB[i]["score"] = 0

    def FileSearch(self, startdirectory, depth=3):
        import magic
        fileDic = {}
        startdirectory = os.path.abspath(os.path.expanduser(os.path.expandvars(startdirectory)))

        # bu kod stack overflow'dan esinlenildi
        # https://stackoverflow.com/questions/42720627/python-os-walk-to-certain-level
        for root, dirs, files in os.walk(startdirectory):
            if root[len(startdirectory):].count(os.sep) < depth:
                for f in files:
                    item = os.path.join(root, f)
                    try:
                        mim = magic.from_file(item)
                        mim = mim.split(",")[1]
                        fileDic[item] = {"filedir": item, "filetype": mim}
                        if mim == " with CRLF line terminators":
                            fileDic[item] = {"filedir": item, "filetype": "Program Kodu"}
                        if mim == " with no line terminators":
                            fileDic[item] = {"filedir": item, "filetype": "Duz Metin"}
                    except (PermissionError, IndexError):
                        pass

        return fileDic


def main():
    root = Tk()
    root.geometry("820x625+275+25")
    root.resizable(width=FALSE, height=FALSE)
    root.configure(bg="darkslategrey")
    app = Analiz(root)
    root.mainloop()


main()
