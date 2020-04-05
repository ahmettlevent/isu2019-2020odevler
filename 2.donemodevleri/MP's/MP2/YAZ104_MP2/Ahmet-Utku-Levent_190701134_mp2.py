from tkinter import *
from tkinter import messagebox,ttk
import xlrd

class DevamsizlikHesaplayici(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.inituI()
    def inituI(self):
        # Arayuzun Programa tanitimi
        Label(self.parent, text="İstinye Kafeterya Öneri Sistemi", bg="misty rose", font="15").place(x=280, y=0)
        Label(self.parent, bg="brown4").place(x=0, y=25, width=800, height=3)

        Label(self.parent, bg="misty rose", text="Müşteri Değerlendirmelerini Yükle").place(x=5, y=33)
        Label(self.parent, bg="brown4").place(x=0, y=60, width=800, height=3)
        Button(self.parent, text="SEC",command=self.excelsec).place(x=250, y=29, width=50, height=25)

        Label(self.parent, bg="misty rose", text="Kendi Değerlendirmelerim",font="22").place(x=280, y=69, width=217, height=25)


        self.textWidget = Text(self.parent)
        self.textWidget.pack()
        self.textWidget.place(x=65, y=140, width=400, height=200)
        self.textWidget.config(state="disabled") # Text widget'in icine yazma ozelligi kapatildi

        # textWidget'a Scrollbar Ekleme Islemi
        scrollbar = ttk.Scrollbar(self.parent,command = self.textWidget.yview)
        scrollbar.place(x=448, y=140,width=18, height=200)
        self.textWidget['yscrollcommand'] = scrollbar.set
        self.textWidget['font'] = ('consolas', '11')

    def excelsec(self):
        pass


def main():
    root = Tk()
    root.geometry("800x500+270+70")
    root.configure(bg="misty rose")
    root.title("by ahmettlevent")
    app = DevamsizlikHesaplayici(root)
    root.mainloop()


main()
