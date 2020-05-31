import urllib.request

from bs4 import BeautifulSoup


class n11data():

    def __init__(self, urunadi, minfiyat, maxfiyat):
        self.urunadi = urunadi.replace(" ", "+")
        self.urun_sozlugu = dict()
        self.urun_listesi = list()
        self.minfiyat = minfiyat
        self.maxfiyat = maxfiyat
        self.page = 0

    def geturl1(self):
        self.urun_sozlugu = {}
        url = "https://www.n11.com/arama?q={}&minp={}&maxp={}".format(self.urunadi, self.minfiyat, self.maxfiyat)
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
        self.getProductDETAIL(self.urun_listesi[4])

    def getProductDETAIL(self, productname):
        url = self.urun_sozlugu[productname]
        response = urllib.request.urlopen(url=url)
        soup = BeautifulSoup(response.read(), features="html.parser")
        page = soup.find("section", {"class": "uni-content"})
        print(page)


n11 = n11data("Televizyon", 1000, 3000)
n11.geturl1()
