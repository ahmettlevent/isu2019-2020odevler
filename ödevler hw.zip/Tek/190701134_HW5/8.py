print("----------SORU 1----------\n")
asal_carpani_bulunmak_istenen_sayi = int(input("Lütfen Asal Çarpanlarını Bulmak İstediğiniz Sayıyı Giriniz\n "))
asal_sayi_sayisi = int(0)
asal_sayi_listesi=[]
sayinin_carpanlari_listesi = []
def asalfonk( asal_carpani_bulunmak_istenen_sayi):
    for i in range(2, asal_carpani_bulunmak_istenen_sayi):
        for a in range(2, i):
            if (i % a) == 0:
                break
        else:
            asal_sayi_listesi.append(i)   # Girilen Sayıya Kadarki Bütün Asal Çarpanlar Bulundu ve Listeye Eklendi.

    # Alttaki döngü yukarıdaki asal sayıların yardımı ile çarpanları bulup ,  sayinin_carpanlari_listesi'ne ekliyor
    for a in asal_sayi_listesi:
        if asal_carpani_bulunmak_istenen_sayi % a == 0:
            sayinin_carpanlari_listesi.append(a)
    if len(sayinin_carpanlari_listesi) == 0:
        sayinin_carpanlari_listesi.append(asal_carpani_bulunmak_istenen_sayi)
    return sayinin_carpanlari_listesi

asalfonk(asal_carpani_bulunmak_istenen_sayi)

print(sayinin_carpanlari_listesi,"\n")

# ------------------------------ SORU ARASI ------------------------------
print("----------SORU 2----------\n")
i=0
def taban_degisimi(kullanici_sayisi):
    global i
    global bit_listesi
    while kullanici_sayisi >= 2**i:
        i+=1
    i-=1
    b = kullanici_sayisi-(2**i)
    print("{} numaralı bit 1 dir.".format(i))
    if i >= 0 and b>=1 and kullanici_sayisi>=1:
        i =0
        taban_degisimi(b)
taban_degisimi_kullanici_girdi = int(input("Lütfen Onluk Tabandan İkilik Tabana Dönüştürmek İstediğiniz Sayıyı Giriniz.\n"))
print("{} Sayısı için .".format(taban_degisimi_kullanici_girdi))
taban_degisimi(taban_degisimi_kullanici_girdi)




























































































