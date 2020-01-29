class Lot():
    BirimFiyat = "Hisse Birim Fiyatidir.."
    AlimTarihi = "Hisselerin Alinmis Oldugu Tarih."
    HisseAdedi = "Mevcut Alınmıs Hisse Adedi."
    def __init__(self,BirimFiyat,AlimTarihi,HisseAdedi): # Kullanicidan alinan veriler gerekli sekilde islenmistir.
        self.BirimFiyat = float(BirimFiyat)
        self.AlimTarihi = str(AlimTarihi)
        self.HisseAdedi = int(HisseAdedi)
    def __str__(self):
        return "Adlı Hissenin Alım Tarihi {}\nHisse Birim Fiyatı {}\nHisse Adedi {}".format(self.AlimTarihi,self.BirimFiyat,self.HisseAdedi)
    def Blok_Alim_Ucreti(self):
        AlimUcreti = self.BirimFiyat*self.HisseAdedi
        print("Hisse Blogu {} tl verilerek alinmistir.".format(AlimUcreti))
    def Blok_Guncel_Fiyat(self,Guncel_Birim_Fiyat):
        YeniUcret = self.HisseAdedi*Guncel_Birim_Fiyat
        print("Hisse Blogunun Suanki Fiyati {} tl dir.".format(YeniUcret))

#****************************************************************************************************

class Pozisyon():
    PozisyonSahibi = "Bu Pozisyona Sahip Olan Kisidir."
    HisseBloklari = "Pozisyon Sahibi Kisinin Sahip Oldugu Hisse Bloklarinin Listesidir."
    def __init__(self,PozisyonSahibi,HisseBloklariListesi):
        self.PozisyonSahibi = str(PozisyonSahibi)
        self.HisseBloklari = list(HisseBloklariListesi)
    def __str__(self):
        hisseadedi = 0
        toplambedel = 0
        for i in self.HisseBloklari:
            hisseadedi+= i.HisseAdedi
            toplambedel += i.HisseAdedi * i.BirimFiyat
        return "{}'in Sahip Oldugu Toplam Hisse Adedi {} : dir. Toplam Satin Alma Bedeli : {} tl dir.".format(self.PozisyonSahibi,hisseadedi,toplambedel)
    def Toplam_Pozisyon_Bedeli(self):
        toplampoziysonbedeli = 0
        for i in self.HisseBloklari:
            toplampoziysonbedeli += i.HisseAdedi * i.BirimFiyat
        print("{}'in Sahip Oldugu Pozisyon'un Toplam Bedeli {} tl dir.".format(self.PozisyonSahibi,toplampoziysonbedeli))
    def Pozisyon_Guncel_Bedeli(self,guncel_hisse_bedelleri_listesi):
        guncelpozisyonbedeli = 0
        for i in range(len(self.HisseBloklari)):#Sırasıyla Her bir hisse blogu listede kendine es gelen siradaki guncel pozisyon bedeli ile carpilmistir.
            guncelpozisyonbedeli += self.HisseBloklari[i].HisseAdedi * guncel_hisse_bedelleri_listesi[i]
        print("{}'in Sahip Oldugu Pozisyon'un Guncel Toplam Bedeli {} tl dir.".format(self.PozisyonSahibi,guncelpozisyonbedeli))

#****************************************************************************************************

class Portfolyo():
    def __init__(self,PozisyonListesi):
        self.PozisyonListesi = list(PozisyonListesi)
#****************************************************************************************************

def rapor(portfolyo):
    for i in portfolyo:
        print(i)
        for a in range(len(i.HisseBloklari)):
            print("     Hisse Blogu {} : Hissenin Alım Tarihi : {} | Hissenin Birim Fiyati : {} | Hisse Adedi : {}".format(a+1,i.HisseBloklari[a].AlimTarihi,i.HisseBloklari[a].BirimFiyat,i.HisseBloklari[a].HisseAdedi))

#****************************************************************************************************

############ HİSSE BLOKLARI ##############
hisseblogu1,hisseblogu2,hisseblogu3= Lot(375,"07.05.2013",23),Lot(511,"22.11.2019",52),Lot(712,"22.06.2015",52)
hisseblogu4,hisseblogu5,hisseblogu6 = Lot(512,"12.03.2007",36),Lot(446,"21.02.2005",23),Lot(210,"05.01.2019",22)
hisseblogu7,hisseblogu8,hisseblogu9= Lot(263,"05.07.2017",21),Lot(182,"30.05.2011",19),Lot(123,"18.08.2019",16)
hisseblogu10,hisseblogu11,hisseblogu12= Lot(721,"15.07.2012",13),Lot(100,"05.06.2005",10),Lot(553,"21.12.2004",51)
############## Pozisyonlar ###############
AhmetLevent = Pozisyon("Ahmet Utku Levent",[hisseblogu1,hisseblogu2,hisseblogu3])
KaanHelvacikoylu = Pozisyon("Kaan Helvacikoylu",[hisseblogu4,hisseblogu5,hisseblogu6])
Aaron_Swartz = Pozisyon("Aaron Swartz",[hisseblogu7,hisseblogu8,hisseblogu9])
Kevin_Mitnick = Pozisyon("Kevin Mitnick",[hisseblogu10,hisseblogu11,hisseblogu12])
############## Portfolyo #################
Zodiac = Portfolyo([AhmetLevent,KaanHelvacikoylu])
Avengers = Portfolyo([Aaron_Swartz,Kevin_Mitnick])
##########################################

#**************
rapor(Zodiac.PozisyonListesi)
rapor(Avengers.PozisyonListesi)
#**************