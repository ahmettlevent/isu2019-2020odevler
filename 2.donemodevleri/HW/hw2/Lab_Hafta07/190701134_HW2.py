class Matris():
    def __init__(self):
        self.delicious_data = open("delicious_data.txt","r",encoding="utf-8")
        self.etiketListesi= set()
        self.websitelerListesi= list()
        self.etiketsozlugu = dict()

        self.WebSiteleri=list()
        self.GetDATA()
        self.EtiketSozluguOlustur()
    def GetDATA(self):
        for raw_line in self.delicious_data.readlines():
            raw_line = raw_line.replace("\n","")
            split_line = raw_line.split("\t")
            self.WebSiteleri.append(split_line)
            self.EtiketleriAl(split_line)
    def WebsiteleriAl(self,split_line):
        self.websitelerListesi.append(split_line[0])
    def EtiketleriAl(self,split_line):
        self.etiketListesi.add(split_line[3])
        self.etiketListesi.add(split_line[5])
        self.etiketListesi.add(split_line[7])
        self.etiketListesi.add(split_line[9])
        self.etiketListesi.add(split_line[11])
        self.etiketListesi.add(split_line[13])
        self.etiketListesi.add(split_line[15])
        self.etiketListesi.add(split_line[17])
        self.etiketListesi.add(split_line[19])
        self.etiketListesi.add(split_line[21])
        print(self.etiketListesi)

    def EtiketSozluguOlustur(self):
        eklenecekler_sozlugu = {}
        for etiket in self.etiketListesi:
            for site in self.WebSiteleri:
                if etiket in site[2:23]:
                    eklenecekler_sozlugu[etiket] = site[site.index(etiket)]
                    print(etiket,site,site[site.index(etiket)+1])
            self.etiketsozlugu[etiket] = eklenecekler_sozlugu
        print(self.etiketListesi)
    def matris_1(self):
        for i in self.etiketListesi:
            with open("Matris1_190701134.txt","w",encoding="utf-8") as matris_file:
                matris_file.write("Etiketler ")
                for i in self.websitelerListesi:
                    matris_file.write(i+" ")
                for i in self.etiketListesi:
                    matris_file.write(i)


Matrisim = Matris()
Matrisim.matris_1()
