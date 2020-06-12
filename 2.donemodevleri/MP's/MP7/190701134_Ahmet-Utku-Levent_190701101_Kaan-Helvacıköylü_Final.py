import os
import re
import shelve
import time
from tkinter import *
from tkinter import messagebox


# WORD CHECK Decorator --
def wordCheck(func):
    '''
    Bu Decorator'un iki farkli islevi bulunmaktadir
    Kelime uzakligi kriteri icin:
            Kelime uzakliklarini hesaplar ve yeni bir liste dondurur.Kelimeleri kontrol eder.
    Zaman kriteri icin:
            Kelime uzakliklarini hesaplar fakat bunun sonuca faydasi olmayacagindan ,
            bu kriter icin faydasi sadece kelimeleri kontrol etmek olacaktir.
    '''

    def wrapper(self, searchDB, agirlik):
        # stackoverflow'dan re ornegi alinmiştir. https://stackoverflow.com/questions/7881794/dont-split-double-quoted-words-with-python-string-split

        entry = self.userwords.get()
        wordlist = re.findall(r'(\w+|".*?")', entry)
        if len(wordlist) == 0:
            messagebox.showerror("HATA", "Lutfen En Az Bir Kelime Giriniz")
        else:
            wordDB = {}
            for path in searchDB:
                content = (searchDB[path]["content"]).strip().split(' ')
                counter = 0
                score = 0
                word_is_in = []
                for word in content:
                    try:
                        if word == wordlist[counter]:
                            word_is_in.append(word)
                            counter += 1
                        elif word != wordlist[counter] and counter > 0:
                            score += 1
                    except IndexError:
                        break
                if wordlist == word_is_in:
                    searchDB[path]["score"] = score
                    wordDB[path] = searchDB[path]
            return func(self, wordDB, agirlik)

    return wrapper


# Time Calculate Decorator --
def calculatetime(func):
    '''bu decorator'de alinan fonk'un zamani olculur ve yukleniyor,
    saniye surdu gibi laberl lar gui de yerini alir'''
    def wrapper(*args):
        starttime = time.time()
        if str(func.__name__) == "index_create":
            args[0].label1 = Label(args[0].parent, bg="misty rose", text="Yukleniyor . .")
            args[0].label1.grid(row=2, column=3, padx=0, ipady=0, pady=20)
        elif str(func.__name__) == "searchWords":
            args[0].label2 =Label(args[0].parent, bg="misty rose", text="Yukleniyor . .")
            args[0].label2.grid(row=6, column=3, padx=0, ipady=0)
        func(*args)
        if str(func.__name__) == "index_create":
            args[0].label1.destroy()
        elif str(func.__name__) == "searchWords":
            args[0].label2.destroy()
        endtime = time.time()
        result = endtime - starttime
        result = str(result)[:5] + " Saniye Surdu"
        if str(func.__name__) == "index_create":
            Label(args[0].parent, bg="misty rose", text=result).grid(row=2, column=3, padx=0, ipady=0, pady=20)
        elif str(func.__name__) == "searchWords":
            Label(args[0].parent, bg="misty rose", text=result).grid(row=6, column=3, padx=0, ipady=0)

    return wrapper


# -------------------------

class Analiz(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.k_uzaklik = BooleanVar() # kelime uzakligi isteniyorsa true istenmiyosa false
        self.e_zaman = BooleanVar() # erisim zamani isteniyorsa true istenmiyosa false

        self.k_uzaklik_agirlik = IntVar() # kelime uzakligi agiriligi simgelenir default = 1
        self.e_zaman_agirlik = IntVar()# erisim zamani agiriligi simgelenir default = 1

        self.startdir = StringVar() # baslangic dizinidir default kok olarak belirlenmistir
        self.startdir.set(r"/")

        self.derinlik = StringVar() # istenen derinlik belirlenir default 3 , bos birakilamaz
        self.derinlik.set("3")

        self.userwords = StringVar() # kullanicinin aramasini istedigi kelimeler arayuzde bos birakilamaz

        self.initUI()

    def initUI(self):
        # Programin arayuzunu oluşturduk
        Label(self.parent, bg="misty rose", text="Dosya Arayici", width=70).grid(row=0, column=1, pady=10, ipadx=10,
                                                                                 ipady=10, columnspan=3)

        Label(self.parent, bg="misty rose", text="Başlangic Dizini").grid(row=1, column=0, padx=0, pady=15)

        Entry(self.parent, width=55, textvariable=self.startdir).grid(row=1, column=1, ipadx=0, pady=5, columnspan=2)

        Label(self.parent, bg="misty rose", text="Derinlik").grid(row=2, column=1, padx=20, ipady=0)

        Entry(self.parent, width=10, textvariable=self.derinlik).grid(row=2, column=1, padx=0, ipady=0, columnspan=3)

        Button(self.parent, bg="misty rose", text="Index Oluştur", command=self.index_create).grid(row=2, column=2,
                                                                                                   padx=0,
                                                                                                   ipady=0, pady=20)

        Label(self.parent, width=10, text="Kelimeler", height=1).grid(row=3, column=0, ipadx=5, ipady=0)
        Entry(self.parent, width=25, textvariable=self.userwords).grid(row=3, column=1, ipadx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Siralama Kriteri").grid(row=4, column=1, padx=0, pady=15)

        Label(self.parent, bg="misty rose", text="Agirliklar").grid(row=4, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3, textvariable=self.k_uzaklik_agirlik).grid(row=5, columnspan=15, padx=0, ipady=0)

        Entry(self.parent, width=3, textvariable=self.e_zaman_agirlik).grid(row=6, columnspan=15, padx=0, ipady=0)

        Label(self.parent, bg="misty rose", text="Filtre").grid(row=4, column=3, padx=0, ipady=0)

        self.filtre = Listbox(self.parent, bg="misty rose", width=21, height=2)
        self.filtre.grid(row=5, column=3, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", command=self.searchWords, text="Ara").grid(row=5, column=4, padx=0,
                                                                                        ipady=0,
                                                                                        pady=0)

        self.Listbox = Listbox(self.parent, bg="misty rose", width=81, height=15)
        self.Listbox.grid(row=7, column=1, padx=0, ipady=0, sticky='ns')

        Label(self.parent, bg="misty rose", text="Sayfa").grid(row=8, column=1, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="onceki").grid(row=8, column=1, padx=50, ipady=0, pady=0,
                                                                 columnspan=3)

        Label(self.parent, bg="misty rose", text="", width=3, height=1).grid(row=8, column=2, padx=0, ipady=0)

        Button(self.parent, bg="misty rose", text="Sonraki").grid(row=8, column=3, padx=0, ipady=0, pady=0,
                                                                  columnspan=3)

        self.R1 = Checkbutton(self.parent, text="Kelime Uzakligi", variable=self.k_uzaklik)
        self.R1.grid(row=5, column=1)

        self.R2 = Checkbutton(self.parent, text="Erişim Zamani", variable=self.e_zaman)
        self.R2.grid(row=6, column=1, pady=20)

        self.filtre.configure(selectmode=MULTIPLE)
        self.filtre.insert(END, "Duz Metin")
        self.filtre.insert(END, "Program Kodu")

    @calculatetime
    def index_create(self):
        # veriler arayuzden alinir ve gerekli fonk'lar cagirilarak index olusturulur.
        if not (self.derinlik.get() is int()) or not (self.derinlik.get() > 0):
            depth = 3
        else:
            depth = self.derinlik.get()

        if os.path.isdir(self.startdir.get()):
            fileDic = self.FileSearch(self.startdir.get(), depth=depth)
            self.index_it(fileDic)
        else:
            messagebox.showerror("ERROR !", "LUTFEN GECERLI BIR DIZIN GIRIN")

    def index_it(self, fileDic):
        db = shelve.open("veriler")
        for i in fileDic:
            db[i] = {"filedir": fileDic[i]["filedir"], "score": 0, "fileType": fileDic[i]["filetype"],
                     "content": open(i).read(), "m_time": os.stat(i).st_atime_ns}
        db.close()

    @calculatetime
    def searchWords(self):
        '''Bu fonk arama kismindan sorumludur database acilir ve icinden tek tek pathler cekilir, isteklere gore
           degiskenlerin kontrolleri yapilir ve duruma bagli fonk'lara gonderilir.
        '''
        db = shelve.open("veriler")
        searchDB = {}
        newdb = {} # bu sozluk gelen verileri kapsar  , update ile gelen veriler buna eklenir,veri zaten var ise iki
                   # secim yapilmis demektir bu durumda onceki ile simdiki secim toplanir ve agirliklar toplami bulunur.

        if int(self.k_uzaklik_agirlik.get()) is int():
            agirlik_k = self.k_uzaklik_agirlik.get()
        else:
            agirlik_k = 1

        if int(self.e_zaman_agirlik.get()) is int():
            agirlik_e = self.e_zaman_agirlik.get()
        else:
            agirlik_e = 1

        if self.e_zaman.get() != self.k_uzaklik.get():
            if self.e_zaman.get() == True and self.e_zaman_agirlik.get() == 0:
                messagebox.showerror("Hata", "Lutfen Sifirdan Buyuk Bir Agirlik Seciniz")
                return
            if self.k_uzaklik.get() == True and self.k_uzaklik_agirlik.get() == 0:
                messagebox.showerror("Hata", "Lutfen Sifirdan Buyuk Bir Agirlik Seciniz")
                return
        try:
            for i in db:
                if db[i]["fileType"] in self.filtre.selection_get().split("\n"):
                    searchDB[i] = db[i]

            if self.k_uzaklik.get() == True:
                data1 = self.cook_data_k_uzaklik(searchDB, agirlik=agirlik_k)
                newdb.update(data1)
            if self.e_zaman.get() == True:
                data2 = self.cook_data_e_zaman(searchDB, agirlik=agirlik_e)
                for i in data2:
                    try:
                        if newdb[i]:
                            newdb[i]["score"] += data2[i]["score"]
                    except KeyError:
                        newdb[i] = data2[i]

            self.listboxYaz(newdb)

            if self.k_uzaklik.get() == False and self.e_zaman.get() == False:
                messagebox.showerror("Kriter", "Lutfen bir siralama kriteri seciniz")

        except TclError:
            messagebox.showerror("Hata !", "Lutfen bir filtre seciniz")

    def listboxYaz(self, dic):
        'gelen sozlukteki veriler method ve fonk yardimiyla siralanir daha sonra listbox`a eklenir '
        try:
            self.Listbox.delete(0, END)
            sortedlist = sorted(dic.items(), key=lambda x: x[1]['score'], reverse=True)

            for i in sortedlist:
                self.Listbox.insert(END, str(i[0].split(r"\\")[-1]) + " = " + str(i[1]["score"]))
        except Exception as e:
            pass

    @wordCheck
    def cook_data_k_uzaklik(self, searchDB, agirlik):
        '''kelime uzakligina gore skor belirlenir  '''
        uzakliklar = {"max": 0, "min": 0.0000001}# skorda en'leri tutan bir sozluk
        tum_uzakliklar = [] # max ve min uzakligin daha kolay belirlenmesi icin bu degisken tanimlanmistir

        for i in searchDB:
            tum_uzakliklar.append(searchDB[i]["score"])

            if searchDB[i]["score"] == max(tum_uzakliklar):
                uzakliklar["max"] = searchDB[i]["score"]
            elif searchDB[i]["score"] == min(tum_uzakliklar):
                uzakliklar["min"] = searchDB[i]["score"]
        for i in searchDB:
            # kelime skor iliskisi olusturulur ve skorlar belirlenir
            # agirlikta sorun yasandigi icin yorum olarak alindi
            try:
                if searchDB[i]["score"] == 0 :
                    raise  ZeroDivisionError
                searchDB[i]["score"] = (searchDB[i]["score"] - uzakliklar["min"]) / (
                            uzakliklar["max"] - uzakliklar["min"])
                #searchDB[i]["score"] = searchDB[i]["score"]* agirlik
            except ZeroDivisionError:
                searchDB[i]["score"] = 0
                pass
        return searchDB

    @wordCheck
    def cook_data_e_zaman(self, searchDB, agirlik):
        zamanlar = {"max": 0, "min": 0.00000001}
        tum_zamanlar = []


        for i in searchDB:
            '''en yuksek ve en dusuk zaman belirlenir'''
            tum_zamanlar.append(searchDB[i]["m_time"])

            if searchDB[i]["m_time"] == max(tum_zamanlar):
                zamanlar["max"] = searchDB[i]["m_time"]
            elif searchDB[i]["m_time"] == min(tum_zamanlar):
                zamanlar["min"] = searchDB[i]["m_time"]

        for i in searchDB:
            # zaman skor iliskisi olusturulur ve skorlar belirlenir
            # agirlikta sorun yasandigi icin yorum olarak alindi
            try:
                print(searchDB[i]["score"])
                searchDB[i]["score"] = (searchDB[i]["m_time"] - zamanlar["min"]) / (zamanlar["max"] - zamanlar["min"])
                #searchDB[i]["score"] = searchDB[i]["score"]* agirlik
            except ZeroDivisionError:
                searchDB[i]["score"] = 0
                pass
        return searchDB

    def FileSearch(self, startdirectory, depth=3):
        '''Baslangic dizininden gelen listenin icinde derinlik kadar dolanip'''
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
                        mim = mim.split(",")[1]# mimin bizi ilgilendiren kismi aliniyor
                        # dosya tipine gore sozluklere bilgi eklenmistir.
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
