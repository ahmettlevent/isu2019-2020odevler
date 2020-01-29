import os
# Kullanicinin Girdigi Degerlere Uygun Bulunan Dizinlerin Eklenmesi Icin Bir Liste Olusturdum
filedirectory_list = []

# Baslangic Dizini , Dosya Adi ve Dosya Uzantisi Alan Bir Fonksiyon.
def dosyabulucu(baslangicdizini,dosyaadi,uzanti):

    # Eger baslangicdizini adli bir dizin veya klasor var ise True Donecektir.
    if os.path.exists(baslangicdizini) == True:

        # baslangicdizini adli dizindeki her bir klasor veya dizin for dongusunde sirasiyla i olarak tanimlanmistir
        for i in os.listdir(baslangicdizini):

        	# print(baslangicdizini+"/"+i) Programin Dolastigi Butun Dizinleri Gormek Icın Kullanabilirsiniz.

            # Eger Dosya adi ve uzantisi i dosyasina esit ise ve i bir dizin 'degil' ise kullaniciya sunulmak uzere listeye eklenmistir.
            if i ==dosyaadi+uzanti and os.path.isdir(baslangicdizini + "/" + i) == False:
                filedirectory_list.append(baslangicdizini + "/" + i)

            # Eger i aradigimiz dosya degil ise i nin bir dosya olup olmadigi ogrenilir.
            # i eger bir dizin ise i dizini recursive bir sekilde tekrardan fonk'nun icine alinir ve i dizininin altindaki
            # Dosyalar kontrol edilir
            elif os.path.isdir(baslangicdizini+"/"+i) == True:
                dosyabulucu(baslangicdizini+"/"+i,dosyaadi,uzanti)


# Menu
while True:
    # Dizinlerin Verildigi Liste Gelecek Aramalar Icin Temizlenmistir.
    filedirectory_list = []

    # Bu dongude kullanicinin girdigi dizinin varligi kontrol edilmistir.Dizin yok ise tekrar istenmistir.
    while True:
        kullanicidirectory = str(input("\n---------------------------------\nLutfen Bir Baslangic Dizini Girin\nornek('/home/ahmettlevent/Desktop'))\n---------------------------------\n"))
        if os.path.isdir(kullanicidirectory) == True:
            break
        else:
            print("Girdiginiz Dizin Tanimsizdir Lutfen Kontrol Edip Tekrar Deneyin")
            continue


    # Kullanicidan arama yapacagi dosya adi ve uzantisi istenmistir.
    kullanicidosyaadi = str(input("Lutfen Bulmak Istediginiz Dosya Adiniz Giriniz\nornek('pythonodev')\n"))
    kullanicidosyauzantisi = str(input("Lutfen Bulmak Istediginiz Dosyanin Uzantisiniz Giriniz\nornek('.py')\n"))

    #-
    print("Arama Yapiliyor Lutfen Bekleyiniz...\n")
    #-

    # Fonksiyon cagirilmis ve gerekli bilgiler girilmistir.
    dosyabulucu(kullanicidirectory,kullanicidosyaadi,kullanicidosyauzantisi)

    # Eger liste 0'dan buyuk ise dizinler listelenmistir, degil ise kullanici bilgilendirilmistir.
    if len(filedirectory_list) > 0 :
        print("Girdiginiz dosya adi ile ayni addaki dosyalarin mutlak yolu su sekilde bulummustur.\n")
        for i in filedirectory_list:
            print(i,"\n")
    else:
        print("Girdiginiz Bilgiler'e Ait Herhangi Bir Dizin Bulunamamistir\nLutfen Kontrol Edip Tekrar Deneyiniz.")
