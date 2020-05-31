from tkinter import*
from tkinterhtml import HtmlFrame
from bs4 import BeautifulSoup
import urllib.request
class Kumeleme(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.urunadi = StringVar()
        self.urun_sozlugu = dict()
        self.urun_listesi = list()
        self.minfiyat = IntVar()
        self.maxfiyat = IntVar()
        self.page = 0

        self.inituI()
    def inituI(self):

        frame1 = Frame(self.parent)
        frame1.pack()

        Grid.rowconfigure(frame1, 0, weight=1)
        Grid.columnconfigure(frame1, 0, weight=1)
        Grid.rowconfigure(frame1, 1, weight=1)
        Grid.rowconfigure(frame1, 6, weight=25)
        Grid.columnconfigure(frame1, 1, weight=1)

        Label(frame1, bg="misty rose", text="Enter the product name").grid(row = 0, column = 0, sticky = W, pady = 2)
        Entry(frame1,textvariable=self.urunadi).grid(row = 0,column = 0, sticky = W, pady = 2,padx=288,ipadx=95)

        Button(frame1, bg='misty rose', text='Search',command=self.geturl1).grid(row = 2,column = 0, sticky = W, pady = 2,padx=215)

        Label(frame1, bg='misty rose', text="min:" ).grid(row = 3, column = 0, sticky = W, pady = 2)
        self.entrymin= Entry(frame1,textvariable=self.minfiyat)
        self.entrymin.grid(row=3, column=0, sticky=W, pady=2, padx=188, ipadx=133)
        Label(frame1, bg='misty rose', text="max:").grid(row=3, column=1, sticky=W, pady=2)

        self.entrymax= Entry(frame1,textvariable=self.maxfiyat)
        self.entrymax.grid(row=3, column=1, sticky=W, pady=2, padx=118, ipadx=133)

        Label(frame1, bg='misty rose', text="Items:").grid(row = 5, column = 0, sticky = W, pady = 2)
        Label(frame1, bg='misty rose', text="Description:").grid(row=5, column=1, sticky=W, pady=2)

        self.listbox = Listbox(frame1)
        self.listbox.grid(row = 6, column = 0,ipadx=260,ipady=290,sticky=W)
        self.listbox.bind('<<ListboxSelect>>', self.getProductDETAIL)
        self.scrollbarekle(self.listbox)
        self.frame = HtmlFrame(frame1, horizontal_scrollbar="auto")
        self.frame.grid(row=6, column=1, ipady=80, sticky=W)


    def geturl1(self):
        self.urun_listesi = []
        self.urunadi = self.urunadi.get().replace(" ", "+")
        self.urun_sozlugu = {}
        url = "https://www.n11.com/arama?q={}&minp={}&maxp={}".format(self.urunadi, self.minfiyat.get(), self.maxfiyat.get())
        response = urllib.request.urlopen(url=url)
        soup = BeautifulSoup(response.read(), features="html.parser")
        mydivs = soup.find("input", {"id": "pageCount"})

        for i in range(1, int(mydivs.get('value')) + 1):
            url = "https://www.n11.com/arama?q={}&minp={}&maxp={}&pg={}".format(self.urunadi, self.minfiyat,
                                                                                self.maxfiyat, i)
            response = urllib.request.urlopen(url=url)
            soup = BeautifulSoup(response.read(), features="html.parser")
            mydivs = soup.findAll("div", {"class": "pro"})
            for j in mydivs:
                self.urun_listesi.append((j.a.get("title")).strip())
                self.urun_sozlugu[(j.a.get("title")).strip()] = (j.a.get("href"))
        self.listbox.delete(0, END)

        for i in self.urun_listesi:
            self.listbox.insert(END, i)


    def getProductDETAIL(self,evt):
        url = self.urun_sozlugu[self.listbox.get(ACTIVE)]
        response = urllib.request.urlopen(url=url)
        soup = BeautifulSoup(response.read(), features="html.parser")
        page = soup.find("section", {"class": "tabPanelItem details"})

        self.frame.set_content("<html>{}</html>".format(page))
    def scrollbarekle(self, Listbox):
        # Listbox'a scrollbar ekleme
        scrollbar_y = Scrollbar(Listbox, width=12)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=Listbox.yview)
        Listbox.config(yscrollcommand=scrollbar_y.set)

        scrollbar_x = Scrollbar(Listbox, orient='horizontal', width=11)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=Listbox.xview)
        Listbox.config(xscrollcommand=scrollbar_x.set)
def main():
    root = Tk()
    root.geometry("1280x720+485+55")
    root.resizable(width=TRUE, height=TRUE)
    root.configure(bg="black")

    app = Kumeleme(root)
    root.mainloop()
main()