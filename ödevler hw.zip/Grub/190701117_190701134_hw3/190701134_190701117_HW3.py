Dogum_yili = input("Doğduğunuz Yılı Girin.")
Dogum_ayi = int(input("Dogduğunuz Ayı Girin"))
Dogum_gunu = int(input("Doğduğunuz Günü Girin"))
#_____________________________
YY = int(Dogum_yili[2:4])
Yil_kod = (YY+(YY//4))%7
#_____________________________
if Dogum_ayi == 1 or Dogum_ayi == 10:
    Ay_kod = 0
elif Dogum_ayi == 5:
    Ay_kod = 1
elif Dogum_ayi == 8:
    Ay_kod = 2
elif Dogum_ayi == 2 or Dogum_ayi == 3 or Dogum_ayi == 11:
    Ay_kod = 3
elif Dogum_ayi == 6:
    Ay_kod = 4
elif Dogum_ayi == 9 or Dogum_ayi == 12:
    Ay_kod = 5
elif Dogum_ayi == 4 or Dogum_ayi == 7:
    Ay_kod = 6
#_____________________________
Dogum_yili_ilk_iki_rakam = Dogum_yili[:2]
if Dogum_yili_ilk_iki_rakam == '17':
    yuzyil_kod = 4
elif Dogum_yili_ilk_iki_rakam == '18':
    yuzyil_kod = 2
elif Dogum_yili_ilk_iki_rakam == '19':
    yuzyil_kod = 0
elif Dogum_yili_ilk_iki_rakam == '20':
    yuzyil_kod = 6
elif Dogum_yili_ilk_iki_rakam == '21':
    yuzyil_kod = 4
elif Dogum_yili_ilk_iki_rakam == '22':
    yuzyil_kod = 2
elif Dogum_yili_ilk_iki_rakam == '23':
    yuzyil_kod = 0
#_____________________________
Artik_yil = 0
if Dogum_ayi == 1 or Dogum_ayi == 2:
    Dogum_yili = int(Dogum_yili)
    if Dogum_yili %4 == 0 and Dogum_yili %100 != 0:
        Artik_yil = 1
    elif Dogum_yili %4 == 0 and Dogum_yili %100 != 0:
        Artik_yil = 1
#_____________________________
Gun_kodu = int(Dogum_gunu)
#_____________________________
Gun_Numarasi =((Yil_kod+Ay_kod+yuzyil_kod+Gun_kodu)-Artik_yil)%7
if Gun_Numarasi == 1:
    print ("Pazartesi Gününde Doğdunuz :)")
elif Gun_Numarasi == 2:
    print  ("Salı Gününde Doğdunuz :)")
elif Gun_Numarasi == 3:
    print  ("Çarşamba Gününde Doğdunuz :)")
elif Gun_Numarasi == 4:
    print  ("Perşembe Gününde Doğdunuz :)")
elif Gun_Numarasi == 5:
    print  ("Cuma Gününde Doğdunuz :)")
elif Gun_Numarasi == 6:
    print  ("Cumartesi Gününde Doğdunuz :)")
elif Gun_Numarasi == 0:
    print  ("Pazar Gününde Doğdunuz :)")

