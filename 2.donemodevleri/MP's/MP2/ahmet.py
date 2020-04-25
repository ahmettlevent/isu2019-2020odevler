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
        Label(self.parent, text="Ä°stinye Kafeterya Ã–neri Sistemi", bg="misty rose", font="15").place(x=280, y=0)

        # --
        Label(self.parent, bg="olive drab").place(x=0, y=25, width=800, height=3)  # cizgi
        Label(self.parent, bg="peach puff", text="MÃ¼ÅŸteri DeÄŸerlendirmelerini YÃ¼kle", font="20").place(x=0, y=28,
                                                                                                       width=252,
                                                                                                       height=31)
        Button(self.parent, text="SEC", command=self.excel_sec, bg="dark green", fg="white").place(x=250, y=31,
                                                                                                   width=50,
                                                                                                   height=25)

        self.alertlabel = Label(self.parent, bg="red4", fg="white smoke", text="! LÃ¼tfen Bir Dosya SeÃ§in !",
                                font="20")
        self.alertlabel.place(x=420, y=32, width=190, height=20)
        # --

        # ---
        Label(self.parent, bg="olive drab").place(x=0, y=60, width=800, height=3)  # cizgi

        Label(self.parent, bg="peach puff", text="Kendi DeÄŸerlendirmelerim", font="20").place(x=180, y=75, width=215,
                                                                                              height=25)
        Label(self.parent, bg="misty rose", text="Kendi DeÄŸerim", font="10").place(x=218, y=110, width=150,
                                                                                   height=20)
        self.combobox = ttk.Combobox(self.parent, textvariable="Excel SeÃ§in", state="readonly")
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

        #                    Ã–neri Modeli
        Button(self.parent, text="Ã–neri Al", command=self.oneriAl, bg="dark green", fg="white").place(x=210, y=318,
                                                                                                      width=75,
                                                                                                      height=30)
        Label(self.parent, bg="peach puff", fg="gray5", text="Ã–neri Modeli", font="10").place(x=55, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="KullanÄ±cÄ± BazlÄ±",
                    variable=self.OneriModeli_var, value=0).place(x=55, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="ÃœrÃ¼n BazlÄ±",
                    variable=self.OneriModeli_var, value=1).place(x=47, y=230, width=95)

        #                   Benzerlik Olcudu

        Button(self.parent, text="Benzer MÃ¼ÅŸterileri Listele", command=self.benzerMusterileriListele, bg="dark green",
               fg="white").place(
            x=478, y=318, width=145, height=30)

        Label(self.parent, bg="peach puff", fg="gray5", text="Benzerlik Ã–lÃ§Ã¼tÃ¼", font="10").place(x=275, y=182)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Ã–klid",
                    variable=self.BenzerlikOlcudu_Var, value=0).place(x=260, y=210, width=95)

        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Pearson",
                    variable=self.BenzerlikOlcudu_Var, value=1).place(x=267, y=230, width=95)
        Radiobutton(self.parent, bg="misty rose", activebackground="misty rose", text="Jaccard",
                    variable=self.BenzerlikOlcudu_Var, value=2).place(x=266, y=250, width=95)
        # ----

        # Ã‡izgi ve Toplam Ã–neri Adedi

        Label(self.parent, bg="peach puff", text="Toplam Ã–neri Adedi", font="20").place(x=55, y=285,
                                                                                        width=150,
                                                                                        height=25)
        Entry(self.parent, textvariable=self.ToplamOneriAdedi).place(x=215, y=288, width=50, height=20)
        Label(self.parent, bg="olive drab").place(x=0, y=310, width=800, height=3)
        #

        #                  SonuÃ§ Listbox'larÄ± ve Butonlar
        self.OneriAl_Listbox = Listbox(self.parent)
        self.OneriAl_Listbox.place(x=130, y=350, width=240, height=140)
        self.scrollbarekle(self.OneriAl_Listbox)

        # --

        self.BenzerMusteriler_Listbox = Listbox(self.parent)
        self.BenzerMusteriler_Listbox.place(x=430, y=350, width=240, height=140)
        self.scrollbarekle(self.BenzerMusteriler_Listbox)

    def databaseAC(self):
        # Dosyalarda KarÄ±ÅŸÄ±klÄ±k olmamasÄ± iÃ§in database bir alt klasÃ¶re aÃ§Ä±lmÄ±ÅŸtÄ±r .
        import os
        dirname = "190701134_UserDATABASE"
        try:
            os.mkdir(dirname)
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "c")
        except FileExistsError:
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "w")

    def excel_sec(self):
        # Excel SeÃ§imi ve KontrolÃ¼
        try:
            self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                             filetypes=(("Excel file", "*.xlsx"),))
            self.yemekListesiCikar()
            self.alertlabel.destroy()
        except IOError:
            messagebox.showwarning("UyarÄ± ", "LÃ¼tfen GeÃ§erli Bir Dosya SeÃ§in ! ")

    def yemekListesiCikar(self):
        # Yemek Listesi SeÃ§im EkranÄ±
        file = xlrd.open_workbook(self.excelFile_path)
        sayfa = file.sheet_by_name(file.sheet_names()[0])

        # Yemekler Sonra KullanÄ±lmak iÃ§in YemekListesi isimli bir deÄŸiÅŸkene(kÃ¼me) kaydedilmiÅŸtir.
        for i in range(1, sayfa.nrows):
            if sayfa.row(i)[1].value not in self.YemekListesi:
                self.YemekListesi.append(sayfa.row(i)[1].value)
        # SeÃ§im ile Birlikte ArayÃ¼zde bazÄ± deÄŸiÅŸiklikler
        self.combobox.set("Yemekler")
        self.combobox.config(values=self.YemekListesi)
        self.combobox.update()
        Label(self.parent, bg="misty rose", text="HAZIR !").place(x=4, y=110)

    def puanlanmisYemekListesiDuzenle(self):
        # Bu Fonksiyon Yemek listesi Ã¼zerinde gerÃ§ekleÅŸen her bir iÅŸlemden sonra yemek listesinin sÄ±fÄ±rdan dÃ¼zenlenmesi
        # iÃ§in Ã§aÄŸÄ±rÄ±lÄ±r.
        self.puanlanmisyemekler_listbox.delete(0, END)
        for i in self.user_data:
            food_text = pickle.loads(i) + "- Puan : " + str(pickle.loads(self.user_data[i]))
            self.puanlanmisyemekler_listbox.insert(END, food_text)

    def puan_kaldir(self):
        try:
            yemek = self.puanlanmisyemekler_listbox.selection_get()  # seÃ§ilen yemek

            # seÃ§ilen yemekten puan bilgisi atÄ±lÄ±p database de aranÄ±r ve silinir
            del self.user_data[pickle.dumps(yemek.split("-")[0])]
            # o an seÃ§ili olan yemek listbox tan silinir
            self.puanlanmisyemekler_listbox.delete(self.puanlanmisyemekler_listbox.curselection())

        except TclError:
            messagebox.showinfo("UyarÄ±", "LÃ¼tfen Silmek Istediginiz Yemegi Secin")

    def puan_ekle(self):

        try:
            if self.combobox.get() in self.YemekListesi:  # Yemek seÃ§im kontrolÃ¼
                if self.yemekPuani.get() > 10 or self.yemekPuani.get() < 0:  # KullanÄ±cÄ± puan kontrolÃ¼
                    messagebox.showwarning("UyarÄ± !", "LÃ¼tfen 0 ile 10 arasinda bir puan girin.")
                else:
                    # Combobox'tan Yemek , Entry'den Puan bilgisi alÄ±nÄ±p Database'e eklenmiÅŸ ve
                    # Yemek Listbox'Ä± dÃ¼zenlenmek Ã¼zere ilgili fonksiyon Ã§aÄŸÄ±rÄ±lmÄ±ÅŸtÄ±r.
                    self.user_data[pickle.dumps(self.combobox.get())] = pickle.dumps(self.yemekPuani.get())
                    self.puanlanmisYemekListesiDuzenle()
            else:
                messagebox.showwarning("UyarÄ± !", "LÃ¼tfen puan vermek istediÄŸiniz yemeÄŸi seÃ§in !!!")
        except TclError:
            messagebox.showwarning("UyarÄ± !", "Puan AlanÄ± BOÅ BÄ±rakÄ±lamaz !!")

    def oneriAl(self):
        try:
            # Toplam Ã¶neri Adedinin 0 dan bÃ¼yÃ¼k olmasÄ± beklenmektedir.
            if self.ToplamOneriAdedi.get() == 0:
                raise TclError

            self.OneriAl_Listbox.delete(0, END)  # Ã–neri listbox Ä± temizlendi

            # OneriModeli_var eÄŸer 0 ise KullanÄ±cÄ± BazlÄ± Ã¶neri , 1 ise ÃœrÃ¼n bazlÄ± Ã¶neri yapÄ±lacaktÄ±r.
            # Ã–ncelikle Ã¶neri fonksiyonlarÄ±ndan geri dÃ¶nen deÄŸer bir sÃ¶zlÃ¼k yapÄ±sÄ±na dÃ¶nÃ¼ÅŸtÃ¼rÃ¼lÃ¼p , sadece Yemek
            # isimler alÄ±nmÄ±ÅŸtÄ±r daha sonra bu deÄŸerler kullanÄ±cÄ±nÄ±n isteÄŸine gÃ¶re iteration yÃ¶ntemi ile alÄ±nmÄ±ÅŸtÄ±r

            if self.OneriModeli_var.get() == 0:
                # init fonksiyonunda benzerlik Ã¶lÃ§Ã¼tleri isimli bir liste deÄŸiÅŸkeninde ilgili benzerlik Ã¶lÃ§Ã¼tleri
                # fonksiyonlarÄ± bulunmaktadÄ±r ,bu kÄ±sÄ±mda kullanÄ±cÄ±nÄ±n seÃ§tiÄŸi Ã¶lÃ§Ã¼te gÃ¶re listenin o indexindeki
                # fonksiyon , similarity parmetresinin yerini almÄ±ÅŸtÄ±r.

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
            messagebox.showerror("UyarÄ± !", "LÃ¼tfen 0'dan BÃ¼yÃ¼k Bir Ã–neri Adedi Giriniz !")
        except StopIteration:
            pass
        except FileNotFoundError:
            messagebox.showwarning("UyarÄ± ", "LÃ¼tfen GeÃ§erli Bir Dosya SeÃ§in ! ")
        except TypeError:
            pass

    def benzerMusterileriListele(self):

        try:
            # Toplam Ã¶neri Adedinin 0 dan bÃ¼yÃ¼k olmasÄ± beklenmektedir.
            if self.ToplamOneriAdedi.get() == 0:
                raise TclError

            c = 0  # KullanÄ±cÄ±ya Bilgi AmaÃ§lÄ± Counter

            # Ã–ncelikle Ã¶neri fonksiyonlarÄ±ndan geri dÃ¶nen deÄŸer bir sÃ¶zlÃ¼k yapÄ±sÄ±na dÃ¶nÃ¼ÅŸtÃ¼rÃ¼lÃ¼p , sadece MÃ¼ÅŸteri
            # isimler alÄ±nmÄ±ÅŸtÄ±r daha sonra bu deÄŸerler kullanÄ±cÄ±nÄ±n adet isteÄŸine gÃ¶re iteration yÃ¶ntemi ile alÄ±nmÄ±ÅŸtÄ±r

            # init fonksiyonunda benzerlik Ã¶lÃ§Ã¼tleri isimli bir liste deÄŸiÅŸkeninde ilgili benzerlik Ã¶lÃ§Ã¼tleri
            # fonksiyonlarÄ± bulunmaktadÄ±r ,bu kÄ±sÄ±mda kullanÄ±cÄ±nÄ±n seÃ§tiÄŸi Ã¶lÃ§Ã¼te gÃ¶re listenin o indexindeki
            # fonksiyon , similarity parmetresinin yerini almÄ±ÅŸtÄ±r.

            self.BenzerMusteriler_Listbox.delete(0, END)
            benzerlikOlcudu = self.BenzerlikOlcudler[self.BenzerlikOlcudu_Var.get()]

            # MÃ¼ÅŸteriler ve KullanÄ±cÄ± ile arasÄ±ndaki mesafeler listbox'a eklenmiÅŸtir.
            iterator = dict(recommendations.topMatches(self.AllCritics(), "Kullanici",
                                                       similarity=benzerlikOlcudu)).keys().__iter__()

            iterator1 = dict(recommendations.topMatches(self.AllCritics(), "Kullanici",
                                                       similarity=benzerlikOlcudu)).values().__iter__()

            for i in range(self.ToplamOneriAdedi.get()):
                c += 1
                self.BenzerMusteriler_Listbox.insert(END,"{}.SÄ±rada {} - Aradaki Mesafe = {}".format(c,iterator1.__next__()
                                                                                            ,str(iterator.__next__())[:4]))

        except StopIteration:
            pass
        except TclError:
            messagebox.showerror("UyarÄ± !", "LÃ¼tfen 0'dan BÃ¼yÃ¼k Bir Ã–neri Adedi Giriniz !")
        except FileNotFoundError:
            messagebox.showwarning("UyarÄ± ", "LÃ¼tfen GeÃ§erli Bir Dosya SeÃ§in ! ")
        except TypeError:
            pass

    def AllCritics(self):
        # Excelden alÄ±nan veriler ile Critis sÃ¶zlÃ¼ÄŸÃ¼ oluÅŸturulmuÅŸ ve KullanÄ±cÄ±nÄ±n verileri sÃ¶zlÃ¼ÄŸÃ¼n iÃ§ine aktarÄ±lmÄ±ÅŸtÄ±r.
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
            messagebox.showwarning("UyarÄ± !!", "LÃ¼tfen Bir Excel SEÃ‡Ä°NÄ°Z !!")
        # -----------

    def tersYuzCritics(self):
        return recommendations.transformPrefs(self.AllCritics())

    def scrollbarekle(self, Listbox):
        # Listbox'a scrollbar ekleme iÅŸlemini kolaylaÅŸtÄ±rmak amaÃ§lÄ± oluÅŸturulmuÅŸ bir fonksiyon.
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