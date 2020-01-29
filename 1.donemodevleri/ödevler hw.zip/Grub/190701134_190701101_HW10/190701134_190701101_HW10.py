import string # cumleyi punctuation harflerden arindirmak icin string modulu import edilmistir.


#********************************************************************************


def dosyaacilis():# Bu fonksiyonda kullanicinin sorgu yapacagi metin acilmistir.
    global dosya
    while True:
        # eger dosya acilir ise except blogu hic calismayacak ve kullanici dogrudan menuye yonlendirilecektir
        # fakat dosya acilmaz ise try blogunda hata olustugu anda except bloguna atlayip 'continue' ile dongunun
        # kullanicidan tekrar bir dosya adi istenmesi saglanacaktir.
        try:
            dosyaadi = str(input("Lutfen metin dosyaniz icin mutlak veya goreceli bir yol adi giriniz.\n"))
            dosya = open(dosyaadi, "r")
            break
        except(FileNotFoundError):
            print("Dosya Bulunamadi")
            continue
    print("\n------------MENU------------\n")


#********************************************************************************


def dosyaislem():# Bu Fonksiyonda , dosyaacilis fonk'nunda acilmis olan metin dosyasindaki satirlar punctuation karakterlerden temizlenip bir listeye atilmistir.

    global sorgulanacak_metin # Ileride Kullanilacagi icin sorgulanacak metin global olarak tanimlanmistir.

    sorgulanacak_metin = [] # Sorgulanacak olan text metin listesi temizlenmistir.

    for i in dosya: # Metin dosyasinin icindeki her bir kelime sirasiyla '\n' ve 'punctuation' karakterlerden temizlenmis ve cumleler bir listeye atilmistir..
        temizlik = str.maketrans(dict.fromkeys(string.punctuation))
        yeni_string = i.translate(temizlik)
        sorgulanacak_metin.append(yeni_string[:-1])


#********************************************************************************


def esdizimlilik(text_metin,sorgulanacak_kelimeler):
    cumle_listesi = []
    a = int(len(sorgulanacak_kelimeler))
    # Bu dongude metindeki her bir satir icin kullanicinin girdigi karakterlerin varligi degiskenler uzerinden kontrol edilmistir.
    for i in range(len(text_metin)):
        b = 0 # Bu degisken eger kullanicinin girdigi butun kelimeler i cumlesinde var ise b==a durumu olacaktir ve
        # Sonuc olan'cumle_listesi' ne Satir numarasinin girilmesini saglayacaktir , eger kullanicinin girdigi kelimelerden
        # Herhangi biri yok ise b != a durumu olusacak ve o satirin numarasi cumle_listesi'ne eklenmeyecektir.
        for r in sorgulanacak_kelimeler:
            if r.lower() in text_metin[i].lower().split():
                b+=1
            if b == a:
                cumle_listesi.append(i+1)
            if b != a:
                continue
    return cumle_listesi


#********************************************************************************


def main():
    while True:
        giris = int(input("1.SORGU\n2.CIKIS\n"))
        if giris == 1:
            esdizimliliksorgusu = [] # sorgulanacak kelimelerin bulundugu liste sifirlanmistir

            dosyaacilis() # kullanicinin istedigi metini acmasi icin fonk'a yonlendirilmistir.

            dosyaislem()

            #---

            #Assagidaki dongude kullanicidan teker teker sorgulayacagi kelimeleri girmesi istenmistir ve kelimeler bir listeye atilmistir.
            print("Lutfen Esdizimlilik Sorgusu Yapacaginiz Kelimeleri Teker Teker Giriniz\n")
            while True:
                esdizim = str(input("Sonraki kelime icin 'enter' , Sonucu Gormek Icin 'q' tuslayiniz.\n"))

                # Sonuc istenmedigi surece esdizimliliksorgusu adli listeye kullanicinin girdigi anahtar kelimeler eklenecektir.
                if esdizim == "q":
                    break
                else :
                    esdizimliliksorgusu.append(esdizim)


            #---


            # esdizimlilik fonknundan gelen cevap degerindeki satir numaralari bir degiskene atilmistir
            sonuc_satir_numaralari = esdizimlilik(sorgulanacak_metin,esdizimliliksorgusu)


            print("\n{} : Kelimelerinin Bulundugu Cumleler ; ".format(esdizimliliksorgusu))
            for i in sonuc_satir_numaralari: # yukaridaki sonuc_Satir_numaralari listesindeki her bir satir numarasi icin print islemi yapilmistir.
                print("Satir : {} : {}".format(i,sorgulanacak_metin[i-1]))
            dosya.close()  # Dosya ile islem bittigi icin dosya kapatilmistir.

        elif giris == 2: # Kullanici Cikis Secti ise Cikis Yapilir
            print("Cikis Basarili ...")
            exit()

#Ana Fonksiyon Cagiriliyor
main()

