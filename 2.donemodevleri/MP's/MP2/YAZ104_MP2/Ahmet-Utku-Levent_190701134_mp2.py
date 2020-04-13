import dbm
import pickle
from tkinter import *
from tkinter import ttk, filedialog, messagebox

import xlrd

import recommendations


class IstinyeKafeterya(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.yemekPuani = DoubleVar()
        self.YemekListesi = list()
        self.BenzerlikOlcudu_Var = IntVar()

        self.ToplamOneriAdedi = IntVar()
        self.OneriModeli_var = IntVar()
        self.BenzerlikOlcudler = [recommendations.sim_distance, recommendations.sim_pearson,
                                  recommendations.sim_jaccard]

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
        Button(self.parent, text="Öneri Al", command=self.oneriAl, bg="dark green", fg="white").place(x=210, y=318,
                                                                                                      width=75,
                                                                                                      height=30)
        Label(self.parent, bg="peach puff", fg="gray5", text="Öneri Modeli", font="10").place(x=55, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Kullanıcı Bazlı",
                    variable=self.OneriModeli_var, value=0).place(x=55, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Ürün Bazlı",
                    variable=self.OneriModeli_var, value=1).place(x=47, y=230, width=95)

        #                   Benzerlik Olcudu

        Button(self.parent, text="Benzer Müşterileri Listele", command=self.benzerMusterileriListele, bg="dark green",
               fg="white").place(
            x=478, y=318, width=145, height=30)

        Label(self.parent, bg="peach puff", fg="gray5", text="Benzerlik Ölçütü", font="10").place(x=275, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Öklid",
                    variable=self.BenzerlikOlcudu_Var, value=0).place(x=260, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Pearson",
                    variable=self.BenzerlikOlcudu_Var, value=1).place(x=267, y=230, width=95)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Jaccard",
                    variable=self.BenzerlikOlcudu_Var, value=2).place(x=266, y=250, width=95)
        # ----

        # Çizgi ve Toplam Öneri Adedi

        Label(self.parent, bg="peach puff", text="Toplam Öneri Adedi", font="20").place(x=55, y=285,
                                                                                        width=150,
                                                                                        height=25)
        Entry(self.parent, textvariable=self.ToplamOneriAdedi).place(x=215, y=288, width=50, height=20)
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
        # Dosyalarda Karışıklık olmaması için database bir alt klasöre açılmıştır .
        import os
        dirname = "190701134_UserDATABASE"
        try:
            os.mkdir(dirname)
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "c")
        except FileExistsError:
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "w")

    def excel_sec(self):
        # Excel Seçimi ve Kontrolü
        try:
            self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                             filetypes=(("Excel file", "*.xlsx"),))
            self.yemekListesiCikar()
            self.alertlabel.destroy()
        except IOError:
            messagebox.showwarning("Uyarı ", "Lütfen Geçerli Bir Dosya Seçin ! ")

    def yemekListesiCikar(self):
        # Yemek Listesi Seçim Ekranı
        file = xlrd.open_workbook(self.excelFile_path)
        sayfa = file.sheet_by_name(file.sheet_names()[0])

        # Yemekler Sonra Kullanılmak için YemekListesi isimli bir değişkene(küme) kaydedilmiştir.
        for i in range(1, sayfa.nrows):
            if sayfa.row(i)[1].value not in self.YemekListesi:
                self.YemekListesi.append(sayfa.row(i)[1].value)
        # Seçim ile Birlikte Arayüzde bazı değişiklikler
        self.combobox.set("Yemekler")
        self.combobox.config(values=self.YemekListesi)
        self.combobox.update()
        Label(self.parent, bg="misty rose", text="HAZIR !").place(x=4, y=110)

    def puanlanmisYemekListesiDuzenle(self):
        # Bu Fonksiyon Yemek listesi üzerinde gerçekleşen her bir işlemden sonra yemek listesinin sıfırdan düzenlenmesi
        # için çağırılır.
        self.puanlanmisyemekler_listbox.delete(0, END)
        for i in self.user_data:
            food_text = pickle.loads(i) + "- Puan : " + str(pickle.loads(self.user_data[i]))
            self.puanlanmisyemekler_listbox.insert(END, food_text)

    def puan_kaldir(self):
        try:
            yemek = self.puanlanmisyemekler_listbox.selection_get()  # seçilen yemek

            # seçilen yemekten puan bilgisi atılıp database de aranır ve silinir
            del self.user_data[pickle.dumps(yemek.split("-")[0])]
            # o an seçili olan yemek listbox tan silinir
            self.puanlanmisyemekler_listbox.delete(self.puanlanmisyemekler_listbox.curselection())

        except TclError:
            messagebox.showinfo("Uyarı", "Lütfen Silmek Istediginiz Yemegi Secin")

    def puan_ekle(self):

        try:
            if self.combobox.get() in self.YemekListesi:  # Yemek seçim kontrolü
                if self.yemekPuani.get() > 10 or self.yemekPuani.get() < 0:  # Kullanıcı puan kontrolü
                    messagebox.showwarning("Uyarı !", "Lütfen 0 ile 10 arasinda bir puan girin.")
                else:
                    # Combobox'tan Yemek , Entry'den Puan bilgisi alınıp Database'e eklenmiş ve
                    # Yemek Listbox'ı düzenlenmek üzere ilgili fonksiyon çağırılmıştır.
                    self.user_data[pickle.dumps(self.combobox.get())] = pickle.dumps(self.yemekPuani.get())
                    self.puanlanmisYemekListesiDuzenle()
            else:
                messagebox.showwarning("Uyarı !", "Lütfen puan vermek istediğiniz yemeği seçin !!!")
        except TclError:
            messagebox.showwarning("Uyarı !", "Puan Alanı BOŞ Bırakılamaz !!")

    def oneriAl(self):
        try:
            # Toplam öneri Adedinin 0 dan büyük olması beklenmektedir.
            if self.ToplamOneriAdedi.get() == 0:
                raise TclError

            self.OneriAl_Listbox.delete(0, END)  # Öneri listbox ı temizlendi

            # OneriModeli_var eğer 0 ise Kullanıcı Bazlı öneri , 1 ise Ürün bazlı öneri yapılacaktır.
            # Öncelikle öneri fonksiyonlarından geri dönen değer bir sözlük yapısına dönüştürülüp , sadece Yemek
            # isimler alınmıştır daha sonra bu değerler kullanıcının isteğine göre iteration yöntemi ile alınmıştır

            if self.OneriModeli_var.get() == 0:
                # init fonksiyonunda benzerlik ölçütleri isimli bir liste değişkeninde ilgili benzerlik ölçütleri
                # fonksiyonları bulunmaktadır ,bu kısımda kullanıcının seçtiği ölçüte göre listenin o indexindeki
                # fonksiyon , similarity parmetresinin yerini almıştır.

                iterator = dict(recommendations.getRecommendations(self.AllCritics(), "Kullanici",
                                                                   similarity=self.BenzerlikOlcudler[
                                                                       self.BenzerlikOlcudu_Var.get()])).values().__iter__()
                for i in range(self.ToplamOneriAdedi.get()):
                    self.OneriAl_Listbox.insert(END, iterator.__next__())

            elif self.OneriModeli_var.get() == 1:

                itemsimilarity = recommendations.calculateSimilarItems(self.AllCritics())
                iterator = dict(recommendations.getRecommendedItems(self.AllCritics(), itemsimilarity,
                                                                         "Kullanici")).values().__iter__()

                for i in range(self.ToplamOneriAdedi.get()):
                    self.OneriAl_Listbox.insert(END, iterator.__next__())

        except TclError:
            messagebox.showerror("Uyarı !", "Lütfen 0'dan Büyük Bir Öneri Adedi Giriniz !")
        except StopIteration:
            pass
        except FileNotFoundError:
            messagebox.showwarning("Uyarı ", "Lütfen Geçerli Bir Dosya Seçin ! ")
        except TypeError:
            pass

    def benzerMusterileriListele(self):

        try:
            # Toplam öneri Adedinin 0 dan büyük olması beklenmektedir.
            if self.ToplamOneriAdedi.get() == 0:
                raise TclError

            c = 0  # Kullanıcıya Bilgi Amaçlı Counter

            # Öncelikle öneri fonksiyonlarından geri dönen değer bir sözlük yapısına dönüştürülüp , sadece Müşteri
            # isimler alınmıştır daha sonra bu değerler kullanıcının adet isteğine göre iteration yöntemi ile alınmıştır

            # init fonksiyonunda benzerlik ölçütleri isimli bir liste değişkeninde ilgili benzerlik ölçütleri
            # fonksiyonları bulunmaktadır ,bu kısımda kullanıcının seçtiği ölçüte göre listenin o indexindeki
            # fonksiyon , similarity parmetresinin yerini almıştır.

            self.BenzerMusteriler_Listbox.delete(0, END)
            benzerlikOlcudu = self.BenzerlikOlcudler[self.BenzerlikOlcudu_Var.get()]

            # Müşteriler ve Kullanıcı ile arasındaki mesafeler listbox'a eklenmiştir.
            iterator = dict(recommendations.topMatches(self.AllCritics(), "Kullanici",
                                                       similarity=benzerlikOlcudu)).keys().__iter__()

            iterator1 = dict(recommendations.topMatches(self.AllCritics(), "Kullanici",
                                                       similarity=benzerlikOlcudu)).values().__iter__()

            for i in range(self.ToplamOneriAdedi.get()):
                c += 1
                self.BenzerMusteriler_Listbox.insert(END,"{}.Sırada {} - Aradaki Mesafe = {}".format(c,iterator1.__next__()
                                                                                            ,str(iterator.__next__())[:4]))

        except StopIteration:
            pass
        except TclError:
            messagebox.showerror("Uyarı !", "Lütfen 0'dan Büyük Bir Öneri Adedi Giriniz !")
        except FileNotFoundError:
            messagebox.showwarning("Uyarı ", "Lütfen Geçerli Bir Dosya Seçin ! ")
        except TypeError:
            pass

    def AllCritics(self):
        # Excelden alınan veriler ile Critis sözlüğü oluşturulmuş ve Kullanıcının verileri sözlüğün içine aktarılmıştır.
        try:
            file = xlrd.open_workbook(self.excelFile_path)
            sayfa = file.sheet_by_name(file.sheet_names()[0])

            KullaniciPuanlari_Dic = dict()
            KullaniciPuanlari_Dic["Kullanici"] = {}

            for i in range(1, sayfa.nrows):
                KullaniciPuanlari_Dic[sayfa.row(i)[0].value] = {}
            for i in range(1, sayfa.nrows):
                KullaniciPuanlari_Dic[sayfa.row(i)[0].value][sayfa.row(i)[1].value] = sayfa.row(i)[2].value

            for i in self.user_data:
                KullaniciPuanlari_Dic["Kullanici"][pickle.loads(i)] = pickle.loads(self.user_data[i])

            return KullaniciPuanlari_Dic
        except AttributeError:
            messagebox.showwarning("Uyarı !!", "Lütfen Bir Excel SEÇİNİZ !!")
        # -----------

    def tersYuzCritics(self):
        return recommendations.transformPrefs(self.AllCritics())

    def scrollbarekle(self, Listbox):
        # Listbox'a scrollbar ekleme işlemini kolaylaştırmak amaçlı oluşturulmuş bir fonksiyon.
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
