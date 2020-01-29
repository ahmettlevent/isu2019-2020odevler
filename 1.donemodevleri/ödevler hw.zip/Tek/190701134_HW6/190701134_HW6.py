import random
#-------------------------
alfabe_mix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabe = " ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Stringler 0.indexten başladığı için bir boşluk bıraktım
rakam_str = "0123456789"
rakam_list= list(rakam_str)

#Alfabedeki harfleri yeni alfabeye atacağım için büyük ve küçük harf olmak üzere iki liste oluşturdum ve atadım.
alfabe_mix_lower = list(alfabe_mix.lower())
alfabe_mix_upper = list(alfabe_mix.upper())

#Rakamlarıda Listeye Atadım
rakam_mix ="0123456789"
rakam_mix_l = list(rakam_mix)
#--------------------------
#Listeleri Karıştırdım ve Yeni Alfabe ile Rakam Listesi Elde Ettim
random.shuffle(alfabe_mix_lower)
random.shuffle(alfabe_mix_upper)
random.shuffle(rakam_mix_l)
#-------------------------
#Karıştırılmış Listeler
#   print(alfabe_mix_upper)
#   print(alfabe_mix_lower)
#   print(rakam_mix_l)
#   print(rakam_list)
#--------------------------
Anahtar =""
Sifreli_kelime =""
Sifresi_Cozulmus_Kelime =""
#--------------------------
def sifreleme_fonk(kullanici_kelimesi):
    global Anahtar
    global Sifreli_kelime
    global Sifresi_Cozulmus_Kelime
    for her_harf in kullanici_kelimesi:
        if her_harf in alfabe_mix_upper :
            harf_rakam = ord(her_harf)- 64
            harf_rakam_2=ord(alfabe_mix_upper[harf_rakam-1])-64
            toplam = harf_rakam+harf_rakam_2
            if toplam > 52:
                toplam -= 52
            elif toplam >= 27:
                toplam -= 26
            Sifreli_kelime += alfabe[toplam]
            Anahtar += chr(harf_rakam_2+64)
            harf_rakam =0
            harf_rakam_2 =0
        elif her_harf in alfabe_mix_lower :
            harf_rakam = ord(her_harf) - 96
            harf_rakam_2 = ord(alfabe_mix_lower[harf_rakam - 1]) - 96
            toplam = harf_rakam + harf_rakam_2
            if toplam > 52:
                toplam -= 52
            elif toplam >= 27:
                toplam -= 26
            Sifreli_kelime += alfabe.lower()[toplam]
            Anahtar +=chr(harf_rakam_2+96)
            harf_rakam = 0
            harf_rakam_2 = 0
        elif her_harf in rakam_mix_l:
            her_harf =int(her_harf)
            harf_rakam = her_harf
            harf_rakam_2 = rakam_mix_l[her_harf]
            harf_rakam_2 = int(harf_rakam_2)
            toplam = harf_rakam + harf_rakam_2
            if toplam > 19:
                toplam -= 10
            elif toplam > 9:
                toplam -= 10
            Sifreli_kelime += rakam_list[toplam]
            Anahtar+=chr(harf_rakam_2+48)

            harf_rakam = 0
            harf_rakam_2 = 0
def sifrecozme_fonk(sifrelenmis_kelime,kelime_anahtari):
    i=0
    global Sifresi_Cozulmus_Kelime
    for her_harf in sifrelenmis_kelime:
        if her_harf in alfabe_mix_upper:
            if sifrelenmis_kelime[i] == kelime_anahtari[i]:
                Sifresi_Cozulmus_Kelime += "Z"
                i+=1
            else:
                uncrypted = ord(sifrelenmis_kelime[i]) - ord(kelime_anahtari[i])
                while uncrypted < 0:
                    uncrypted+=26
                uncrypted = chr(uncrypted+64)
                Sifresi_Cozulmus_Kelime += uncrypted
                i += 1
        elif her_harf in alfabe_mix_lower:
            if sifrelenmis_kelime[i] == kelime_anahtari[i]:
                Sifresi_Cozulmus_Kelime += "z"
                i+=1
            else:
                uncrypted = ord(sifrelenmis_kelime[i]) - ord(kelime_anahtari[i])
                while uncrypted < 0:
                    uncrypted+=26
                uncrypted = chr(uncrypted+96)
                Sifresi_Cozulmus_Kelime += uncrypted
                i += 1
        elif her_harf in rakam_list:
            uncrypted = ord(sifrelenmis_kelime[i]) - ord(kelime_anahtari[i])
            while uncrypted < 0:
                uncrypted += 10
            if uncrypted > 9:
                uncrypted-=10
            uncrypted = chr(uncrypted + 48)
            Sifresi_Cozulmus_Kelime += uncrypted
            i += 1



# Menücüğüüüm :9
while True:
    print("------MENÜ------\n1.Şifreleme\n2.Şifre Çözme\n3.Çıkış\n--------------")
    kullanici_giris = int(input(""))

    if kullanici_giris == 1:
        kullanici_message = input("Lütfen Şifrelemek İstediğiniz Metni Giriniz\n")
        sifreleme_fonk(kullanici_message)
        print("Metnin Şifrelenmiş Hali :", Sifreli_kelime)
        print("Metninizin Anahtarı :",Anahtar)
        Sifreli_kelime = ""
        Anahtar = ""

    elif kullanici_giris ==2 :
        kullanici_message_2 = input("Lütfen Şifresini Çözmek İstediğiniz Metni Girin\n")
        kullanici_message_3 = input("Lütfen Metnin Anahtarını Girin\n")
        sifrecozme_fonk(kullanici_message_2,kullanici_message_3)
        print("Şifrenin Çözülmüş Hali :", Sifresi_Cozulmus_Kelime)
        Sifresi_Cozulmus_Kelime =""

    elif kullanici_giris ==3:
        exit()