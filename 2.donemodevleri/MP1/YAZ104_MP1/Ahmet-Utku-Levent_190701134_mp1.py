from tkinter import *
from tkinter import messagebox,ttk

import xlrd

class DevamsizlikHesaplayici(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        # Kullanicidan alinan esik degerinin kullanimi icin sinifa ait bir Double degiskeni,ve Sonuc icin degiskenler
        self.dersEsigi = DoubleVar()
        self.kalan_ogrenci_sayisi = 0 # Toplam kalan ogrenci sayisini belirtir
        self.oturumdan_dolayi_kalanlar = [0, 0] # 2 Oturumda kalan ogrenci sayilari bu listede saklanir oturum 
                                                # sayisini artirmak icin listeye 0 eklemek yeterlidir.

        self.inituI()
    def inituI(self):
        # Arayuzun Programa tanitimi
        Label(self.parent, text="Devamsizlik Hesaplayici", bg="misty rose", font="15").place(x=163, y=0, width=200,
                                                                                             height=25)
        Label(self.parent, bg="brown4").place(x=0, y=25, width=550, height=3)
        Label(self.parent, bg="misty rose", text="Lutfen Bir Excel Dosyasi Seciniz").place(x=0, y=35, width=220,
                                                                                           height=25)
        Button(self.parent, text="SEC", command=self.excelFileOpener).place(x=250, y=35, width=50, height=25)
        Label(self.parent, bg="misty rose")

        Label(self.parent, bg="misty rose", text="Devamsizliktan Kalma Esigi  %").place(x=0, y=69, width=217, height=25)
        Entry(self.parent, bg="white", textvar=self.dersEsigi).place(x=250, y=69, width=50, height=25)

        Label(self.parent, bg="brown4").place(x=0, y=102, width=550, height=3)
        Button(self.parent, text="HESAPLA", command=self.hesapla).place(x=95, y=109, width=80, height=25)

        Button(self.parent, text="TEMIZLE", command=self.temizle).place(x=340, y=109, width=80, height=25)

        self.textWidget = Text(self.parent)
        self.textWidget.pack()
        self.textWidget.place(x=65, y=140, width=400, height=200)
        self.textWidget.config(state="disabled") # Text widget'in icine yazma ozelligi kapatildi

        # textWidget'a Scrollbar Ekleme Islemi
        scrollbar = ttk.Scrollbar(self.parent,command = self.textWidget.yview)
        scrollbar.place(x=448, y=140,width=18, height=200)
        self.textWidget['yscrollcommand'] = scrollbar.set
        self.textWidget['font'] = ('consolas', '11')
    def excelFileOpener(self):
        # Kullanicinin sectigi dosyanin mutlak yolu daha sonra dosyayi acmak icin degiskene atanmistir.
        from tkinter import filedialog
        self.excelFile = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                    filetypes=(("Excel file", "*.xlsx"),))

    def hesapla(self):
        # Boolean tipindeki Widget olustur degiskenimiz ile eger program hata verirse kullaniciya sonuc ekraninin
        # verilip verilmeyecegini kontrol ediyoruz,herhangi bir sorun olmadikca deger True kalacaktir
        self.widget_olustur = True
        try:
            # Yanlis deger girilmesi durumunda ValueError firlatip 0 ile 100 arasinda deger girilmesi isteniyor
            if self.dersEsigi.get() > 100 or self.dersEsigi.get() < 0:
                raise ValueError
            # Kullanicinin dosya secmeden devam etmesidurumunda programda kendiliginden Attribute Error olusturacaktir
            # ve Eger kullanici dosya secme yerini acip yinede secmez ise bu sefer Attribute Error raise edilecektir
            # Her iki durum icinde program except blogunda ilgili bolume girecektir .
            if len(self.excelFile) == 0:
                raise AttributeError

            # Programda aldigimiz dosyanin mutlak yolunu xlrd modulune yonlendirdik.Devaminda ise veriyi isledik
            excelfile = xlrd.open_workbook(self.excelFile)

            sheets = excelfile.sheet_names()
            for i in sheets:
                excel_sayfasi = excelfile.sheet_by_name(i)
                self.kalan_ogrenci_sayisi = 0  # Dersten Kalan Ogrenci Sayisi
                self.oturumdan_dolayi_kalanlar = [0, 0]
                for k in range(1, excel_sayfasi.nrows): # excel_sayfasi.nrows=Ilk Excel Sayfasindaki Toplam Satir sayisi
                    gelinen_gun_sayisi = 0 # her satir bir ogrencidir bu yuzden her seferinde gun sayisi sifirlanir

                    # Eger excel'de Ogrencinin numarasi var ise if bloguna girecektir fakat numarasi yok ise
                    # TypeError hatasi olusacak ve son ogrenci olarak dusunulup hesaplama islemi duracaktir.
                    if excel_sayfasi.row(k)[0].value >= 0:

                        # Ogrencinin 14 gun boyunca her gun icin gelip gelmedigi tek tek kontrol edilip degiskene atanir
                        # daha sonrasinda eger ogrencinin katilim ortalamasi ders esiginden dusuk ise farkli bir
                        # if bloguna girecek ve kalan ogrenci sayisi ile hangi oturumda ise o oturumda kalan toplam
                        # ogrenci sayisi bir artilacaktir, (listenin 0. indexi 1. oturum olarak dusunulmustur)
                        # !!!! program sadece 2 oturum olarak dusunulmustur.
                        for j in range(6, 20):
                            if str(excel_sayfasi.row(k)[j])[6:7] == "X":
                                gelinen_gun_sayisi += 1
                        if gelinen_gun_sayisi * (100 / 14) < int(self.dersEsigi.get()):
                            self.kalan_ogrenci_sayisi += 1
                            self.oturumdan_dolayi_kalanlar[int(excel_sayfasi.row(k)[1].value)-1] +=1

        except (ValueError, TclError):
            messagebox.showerror("Yanlis Giris", "Esik Degeri 0 ile 100 Arasinda Olmalidir !!")
            self.widget_olustur = False
        except AttributeError:
            messagebox.showerror("uyari", "Lutfen Secimlerinizi Kontrol Edin !!")
            self.widget_olustur = False
        except TypeError:
            pass
        finally:
            # Widget'a ekleme islemi herturlu denenecektir
            self.widgeta_ekle()

    def widgeta_ekle(self):
        # Eger Hersey yolunda ise , self.widget_olustur True'dur
        '''
        Widget in write modu acilmis ve sonuclar TextWidget icine yazilmis daha sonra bu ozellik kapatilmistir.
        '''
        if self.widget_olustur is True:

            self.textWidget.config(state="normal")
            # ---------------   Text Widget ekleme islemi
            self.textWidget.insert(INSERT,"--\n{} Esik Puani Icin\nDersten Kalan Ogrenci Sayisi = {}\n"
                                   .format(self.dersEsigi.get(),str(self.kalan_ogrenci_sayisi)))
            for i in range(len(self.oturumdan_dolayi_kalanlar)):
                self.textWidget.insert(INSERT,"{}. Oturumda olup kalan ogrenci sayisi = {}\n"
                                       .format(i+1,self.oturumdan_dolayi_kalanlar[i]))
            # ---------------
            self.textWidget.config(state="disabled")

    def temizle(self):
        '''
        Programdaki ogrenciler ile alakali butun degiskenler kullanilablir duruma getirilmis ve
        TextWidget'in yazma durumu acilip temizlenmistir daha sonra yazma ozelligi kapatilmistir.
        '''
        self.oturumdan_dolayi_kalanlar = []
        self.kalan_ogrenci_sayisi = 0

        self.textWidget.config(state="normal")
        self.textWidget.delete('1.0', END)
        self.textWidget.config(state="disabled")


def main():
    root = Tk()
    root.geometry("530x380+470+180")
    root.configure(bg="misty rose")
    root.title("by ahmettlevent")
    app = DevamsizlikHesaplayici(root)
    root.mainloop()


main()
