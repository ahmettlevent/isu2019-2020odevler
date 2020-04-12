import dbm
import pickle
from tkinter import *
from tkinter import ttk, filedialog, messagebox

import xlrd


class IstinyeKafeterya(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.yemekPuani = DoubleVar()
        self.YemekListesi = list()
        self.KullaniciPuanlari_Dic = dict()

        self.ToplamOneriAdedi = IntVar()

        self.OneriModeli_var = BooleanVar()
        self.BenzerlikOlcudu_Var = BooleanVar()

        self.databaseAC()
        self.inituI()
        self.puanlanmisYemekListesiDuzenle()

    def inituI(self):
        # Arayuzun Programa tanitimi
        Label(self.parent, text="İstinye Kafeterya Öneri Sistemi", bg="misty rose", font="15").place(x=280, y=0)

        # --
        Label(self.parent, bg="olive drab").place(x=0, y=25, width=800, height=3)  # cizgi
        Label(self.parent, bg="peach puff", text="Müşteri Değerlendirmelerini Yükle", font="20").place(x=0, y=28,
                                                                                                       width=252,
                                                                                                       height=31)
        Button(self.parent, text="SEC", command=self.excel_sec, bg="dark green", fg="white").place(x=250, y=31,
                                                                                                   width=50,
                                                                                                   height=25)

        self.alertlabel = Label(self.parent, bg="red4", fg="white smoke", text="! Lütfen Bir Dosya Seçin !",
                                font="20")
        self.alertlabel.place(x=420, y=32, width=190, height=20)
        # --

        # ---
        Label(self.parent, bg="olive drab").place(x=0, y=60, width=800, height=3)  # cizgi

        Label(self.parent, bg="peach puff", text="Kendi Değerlendirmelerim", font="20").place(x=180, y=75, width=215,
                                                                                              height=25)
        Label(self.parent, bg="misty rose", text="Kendi Değerim", font="10").place(x=218, y=110, width=150,
                                                                                   height=20)
        self.combobox = ttk.Combobox(self.parent, textvariable="Excel Seçin", state="readonly")
        self.combobox.place(x=60, y=110, width=170, height=20)
        Entry(self.parent, textvariable=self.yemekPuani).place(x=352, y=110, width=50, height=20)
        Button(self.parent, text="EKLE", command=self.puan_ekle, bg="dark green", fg="white").place(x=405, y=110,
                                                                                                    width=50,
                                                                                                    height=20)
        # Listbox ve Scrollbar
        self.puanlanmisyemekler_listbox = Listbox(self.parent)
        self.puanlanmisyemekler_listbox.place(x=460, y=110, width=240, height=140)
        self.scrollbarekle(self.puanlanmisyemekler_listbox)

        Button(self.parent, text="SECILIYI\nKALDIR", command=self.puan_kaldir, bg="dark green", fg="white").place(x=710,
                                                                                                                  y=110,
                                                                                                                  width=75,
                                                                                                                  height=30)
        # ---

        # Radio Button ve Listboxlar
        # ----
        Label(self.parent, bg="olive drab", fg="white", text="AYARLAR", font="10").place(x=0, y=160, width=462,
                                                                                         height=20)

        #                    Öneri Modeli
        Label(self.parent, bg="peach puff", fg="gray5", text="Öneri Modeli", font="10").place(x=55, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Kullanıcı Bazlı",
                    variable=self.OneriModeli_var, value=1).place(x=55, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Ürün Bazlı",
                    variable=self.OneriModeli_var, value=2).place(x=47, y=230, width=95)

        #                   Benzerlik Olcudu
        Label(self.parent, bg="peach puff", fg="gray5", text="Benzerlik Ölçütü", font="10").place(x=275, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Öklid",
                    variable=self.BenzerlikOlcudu_Var, value=1).place(x=260, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Pearson",
                    variable=self.BenzerlikOlcudu_Var, value=2).place(x=267, y=230, width=95)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Jaqqard",
                    variable=self.BenzerlikOlcudu_Var, value=3).place(x=266, y=250, width=95)
        # ----

        # Çizgi ve Toplam Öneri Adedi

        Label(self.parent, bg="peach puff", text="Toplam Öneri Adedi", font="20").place(x=55, y=285,
                                                                                        width=150,
                                                                                        height=25)
        Entry(self.parent, textvariable=self.ToplamOneriAdedi).place(x=215, y=288, width=50,height=20)
        Label(self.parent, bg="olive drab").place(x=0, y=310, width=800, height=3)
        #

        #                  Sonuç Listbox'ları ve Butonlar
        self.OneriAl_Listbox = Listbox(self.parent)
        self.OneriAl_Listbox.place(x=130, y=350, width=240, height=140)
        self.scrollbarekle(self.OneriAl_Listbox)

        # --

        self.BenzerMusteriler_Listbox = Listbox(self.parent)
        self.BenzerMusteriler_Listbox.place(x=430, y=350, width=240, height=140)
        self.scrollbarekle(self.BenzerMusteriler_Listbox)

    def databaseAC(self):
        import os
        dirname = "190701134_UserDATABASE"
        try:
            os.mkdir(dirname)
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "c")
        except FileExistsError:
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "w")

    def excel_sec(self):
        try:
            self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                             filetypes=(("Excel file", "*.xlsx"),))
            self.yemekListesiCikar()
            self.alertlabel.destroy()
        except IOError:
            messagebox.showwarning("Lütfen Geçerli Bir Dosya Seçin ! ")

    def yemekListesiCikar(self):
        file = xlrd.open_workbook(self.excelFile_path)
        sayfa = file.sheet_by_name(file.sheet_names()[0])
        for i in range(1, sayfa.nrows):
            if sayfa.row(i)[1].value not in self.YemekListesi:
                self.YemekListesi.append(sayfa.row(i)[1].value)
        self.combobox.set("Yemekler")
        self.combobox.config(values=self.YemekListesi)
        self.combobox.update()
        Label(self.parent, bg="misty rose", text="HAZIR !").place(x=4, y=110)

    def musteriDegerlendirmeleriniCikar(self):
        file = xlrd.open_workbook(self.excelFile_path)
        sayfa = file.sheet_by_name(file.sheet_names()[0])

        yemek_puanlari = {}  # Her bir yemek icin kullanicilarin verdigi puanlar
        for a in range(1, sayfa.nrows):
            for i in range(1, sayfa.nrows):
                yemek_puanlari[sayfa.row(i)[0].value] = sayfa.row(i)[2].value  # yemek icin verilen puanlar sozlukte
            self.KullaniciPuanlari_Dic[sayfa.row(a)[1].value] = yemek_puanlari  # genel sozluge eklendi
            yemek_puanlari = {}  # onceki yemegin puanlari silinmistir

    def puanlanmisYemekListesiDuzenle(self):
        self.puanlanmisyemekler_listbox.delete(0, END)
        for i in self.user_data:
            food_text = pickle.loads(i) + " - Puan : " + str(pickle.loads(self.user_data[i]))
            self.puanlanmisyemekler_listbox.insert(END, food_text)

    def puan_kaldir(self):
        try:
            yemek = self.puanlanmisyemekler_listbox.selection_get()
            del self.user_data[pickle.dumps(yemek[:-12])]
            self.puanlanmisyemekler_listbox.delete(self.puanlanmisyemekler_listbox.curselection())
        except:
            messagebox.showinfo("Uyarı", "Lütfen Silmek Istediginiz Yemegi Secin")

    def puan_ekle(self):
        try:
            if len(self.combobox.get()) > 0 and self.combobox.get() in self.YemekListesi:
                if self.yemekPuani.get() > 10 or self.yemekPuani.get() < 0:
                    messagebox.showwarning("Uyarı !", "Lütfen 0 ile 10 arasinda bir puan girin.")
                else:
                    self.user_data[pickle.dumps(self.combobox.get())] = pickle.dumps(self.yemekPuani.get())
                    self.puanlanmisYemekListesiDuzenle()
            else:
                messagebox.showwarning("Uyarı !", "Lütfen puan vermek istediğiniz yemeği seçin !!!")
        except TclError:
            messagebox.showwarning("Uyarı !", "Puan Alanı BOŞ Bırakılamaz !!")

    def scrollbarekle(self, Listbox):
        scrollbar_y = Scrollbar(Listbox, width=12)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=Listbox.yview)
        Listbox.config(yscrollcommand=scrollbar_y.set)
        Listbox.config(yscrollcommand=scrollbar_y.set)


def main():
    root = Tk()
    root.geometry("800x500+285+85")
    root.resizable(width=False, height=False)
    root.configure(bg="misty rose")
    root.title("by ahmettlevent")
    app = IstinyeKafeterya(root)
    root.mainloop()


main()
