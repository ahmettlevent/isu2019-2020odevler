import dbm
import xlrd
from tkinter import *
from tkinter import ttk, filedialog


class DevamsizlikHesaplayici(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.YemekListesi = []
        self.KullaniciPuanlari_Dic = dict()

        self.yemekListesiCikar()
        self.musteriDegerlendirmeleriniCikar()
        self.db_create()

        self.inituI()

    def inituI(self):
        # Arayuzun Programa tanitimi
        Label(self.parent, text="İstinye Kafeterya Öneri Sistemi", bg="misty rose", font="15").place(x=280, y=0)
        # --
        Label(self.parent, bg="olive drab").place(x=0, y=25, width=800, height=3)  # cizgi
        Label(self.parent, bg="peach puff", text="Müşteri Değerlendirmelerini Yükle", font="20").place(x=0, y=28,
                                                                                                       width=252,
                                                                                                       height=31)
        Button(self.parent, text="SEC", command=self.excel_open, bg="dark green", fg="white").place(x=250, y=31,
                                                                                                    width=50,
                                                                                                    height=25)
        # --
        Label(self.parent, bg="olive drab").place(x=0, y=60, width=800, height=3)  # cizgi

        Label(self.parent, bg="peach puff", text="Kendi Değerlendirmelerim", font="20").place(x=180, y=75, width=215,
                                                                                              height=25)
        Label(self.parent, bg="misty rose", text="Kendi Değerim", font="10").place(x=220, y=110, width=150,
                                                                                   height=20)
        Button(self.parent, text="EKLE", command=self.excel_open, bg="dark green", fg="white").place(x=400, y=110,
                                                                                                     width=50,
                                                                                                     height=20)

        ttk.Combobox(self.parent, values=self.YemekListesi
                     , state="readonly", textvariable="Yemekler"
                     ).place(x=60, y=110, width=170, height=20)

        Text(self.parent).place(x=365, y=110, width=25, height=20)

        self.textWidget = Text(self.parent)
        self.textWidget.place(x=65, y=300, width=400, height=55)
        # self.textWidget.config(state="disabled")  # Text widget'in icine yazma ozelligi kapatildi

        # textWidget'a Scrollbar Ekleme Islemi
        scrollbar = ttk.Scrollbar(self.parent, command=self.textWidget.yview)
        scrollbar.place(x=448, y=300, width=18, height=55)
        self.textWidget['yscrollcommand'] = scrollbar.set

    def db_create(self):
        import os
        dirname = "190701134_UserDATABASE"
        try:
            os.mkdir(dirname)
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "c")
        except FileExistsError:
            self.user_data = dbm.open("{}/KullaniciDegerlendirmeleri".format(dirname), "w")

    def excel_open(self):
        self.excelFile_path = filedialog.askopenfilename(initialdir="/", title="Dosya Sec",
                                                         filetypes=(("Excel file", "*.xlsx"),))

    def yemekListesiCikar(self):
        file = xlrd.open_workbook("Musteri_Degerlendirmeleri.xlsx")
        sayfa = file.sheet_by_name(file.sheet_names()[0])
        for i in range(1, sayfa.nrows):
            self.YemekListesi.append(sayfa.row(i)[1].value)

    def musteriDegerlendirmeleriniCikar(self):
        file = xlrd.open_workbook("Musteri_Degerlendirmeleri.xlsx")
        sayfa = file.sheet_by_name(file.sheet_names()[0])

        yemek_puanlari = {}  # Her bir yemek icin kullanicilarin verdigi puanlar
        for a in range(1, sayfa.nrows):
            for i in range(1, sayfa.nrows):
                yemek_puanlari[sayfa.row(i)[0].value] = sayfa.row(i)[2].value  # yemek icin verilen puanlar sozlukte
            self.KullaniciPuanlari_Dic[sayfa.row(a)[1].value] = yemek_puanlari  # genel sozluge eklendi
            yemek_puanlari = {}  # onceki yemegin puanlari silinmistir


def main():
    root = Tk()
    root.geometry("800x500+285+85")
    root.resizable(width=False, height=False)
    root.configure(bg="misty rose")
    root.title("by ahmettlevent")
    app = DevamsizlikHesaplayici(root)
    root.mainloop()


main()
