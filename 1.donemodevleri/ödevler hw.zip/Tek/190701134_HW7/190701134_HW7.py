'''
Tanitim .d
oyuncu_sirasi = O anki oyuncunun kim olduğunu belirlemek için duruma göre 0 ve 1 atanan bir değişkendir.
oyuncu_kim = O anki oyuncunun kim olduğunu belirlemek için duruma göre Birinci ve İkinci stringleri atanan değişkendir.
sutun_satir_dolumu = sutun veya satir dolu ise 1 degerini alan ve kosul bloklarindan kacan degiskendir.
dogruluk = Butun oyun tahtasini tarayip tahta bos ise 0 degerini alan ve oyunun bitmesini saglayan degiskendir.

'''
satir_1,satir_2,satir_3 = ["x","x","x","x","x","x","x"],["x","x","x","x","x","x"," "],["x","x","x","x","x"," "," "]
satir_4,satir_5,satir_6 = ["x","x","x","x"," "," "," "],["x","x","x"," "," "," "," "],["x","x"," "," "," "," "," "]
satir_7 = ["x"," "," "," "," "," "," "]
satir_list=[satir_1,satir_2,satir_3,satir_4,satir_5,satir_6,satir_7]
oyuncu_sirasi = -1
# OYUN TABLOSU
print("--------------------OYUN TAHTASI--------------------")
for i in range(6, -1, -1):
    print("{} {}".format(i + 1, satir_list[i]))
    if i == 0:
        print("0   1", "   2", "   3", "   4", "   5", "   6", "   7")
# ------------
while True:
    print("----------------------------------------------------")
    oyuncu_sirasi +=1
    oyuncu_kim = ""
    dogruluk = 0
    sutun_satir_dolumu = 0
    if oyuncu_sirasi %2 == 0:
        oyuncu_kim += "Birinci Oyuncu "
    elif oyuncu_sirasi %2 == 1:
        oyuncu_kim += "İkinci Oyuncu "
    while True :
        kullanici_girisi  = float(input("1.Satır\n2.Sutun \n{} oynuyor. = ".format(oyuncu_kim)))
        if kullanici_girisi == 1 :
            kullanici_girisi_satir = float(input("Lütfen Silmek İstediğiniz Satir Numarasını Giriniz."))
            if kullanici_girisi_satir == int(kullanici_girisi_satir) and 0 < kullanici_girisi_satir < 8:
                for char in satir_list:
                    for char in range(len(satir_list[int(kullanici_girisi_satir)-1])):
                        if satir_list[int(kullanici_girisi_satir) - 1][char] == "x":
                            sutun_satir_dolumu = 1
                if sutun_satir_dolumu == 1:
                    for char in range(len(satir_list[int(kullanici_girisi_satir)-1])):
                        satir_list[int(kullanici_girisi_satir) - 1][char] = " "
                    for char in satir_list:
                        for i in char:
                            if i == "x":
                                dogruluk = 1
                    if dogruluk == 0:
                        oyuncu_sirasi-=1
                        oyuncu_kim = ""
                        if oyuncu_sirasi % 2 == 0:
                            oyuncu_kim += "Birinci Oyuncu "
                        elif oyuncu_sirasi % 2 == 1:
                            oyuncu_kim += "İkinci Oyuncu "
                        print("{}Oyunu Kazandı Vihuuu :S".format(oyuncu_kim))
                        exit()
                        break
                    print("\t\t\tOYUN TAHTASI\t\t\t")
                    for i in range(6, -1, -1):
                        print("{} {}".format(i + 1, satir_list[i]))
                        if i == 0:
                            print("0   1", "   2", "   3", "   4", "   5", "   6", "   7")
                    break
                elif sutun_satir_dolumu == 0 :
                    print("---\nGirdiğiniz Satir Bos Lütfen Farklı Bir Satir Deneyiniz\n---")
            elif kullanici_girisi_satir != int(kullanici_girisi_satir):
                print("Lütfen Bir Tamsayı Giriniz")
                continue
            elif int(kullanici_girisi_satir) < 1 or int(kullanici_girisi_satir) > 7:
                print("Lütfen 0 ile 8 arasında bir satir numarasi giriniz\n-")
                continue

        elif kullanici_girisi == 2 :
            kullanici_girisi_sutun = float(input("Lütfen Silmek İstediğiniz Sutun Numarasını Giriniz."))
            if kullanici_girisi_sutun == int(kullanici_girisi_sutun) and 0 < kullanici_girisi_sutun < 8:
                for char in satir_list:
                    for satir in char:
                        if char[int(kullanici_girisi_sutun)-1] == "x":
                            sutun_satir_dolumu = 1
                if sutun_satir_dolumu == 1 :
                    for char in satir_list:
                        for satir in char:
                            char[int(kullanici_girisi_sutun)-1] = " "
                    for char in satir_list:
                        for i in char:
                            if i == "x":
                                dogruluk = 1
                    if dogruluk == 0:
                        oyuncu_sirasi -= 1
                        oyuncu_kim = ""
                        if oyuncu_sirasi % 2 == 0:
                            oyuncu_kim += "Birinci Oyuncu "
                        elif oyuncu_sirasi % 2 == 1:
                            oyuncu_kim += "İkinci Oyuncu "
                        print("{}Oyunu Kazandı Vihuuu :S".format(oyuncu_kim))
                        exit()
                        break
                    print("\t\t\tOYUN TAHTASI\t\t\t")
                    for i in range(6, -1, -1):
                        print("{} {}".format(i + 1, satir_list[i]))
                        if i == 0:
                            print("0   1", "   2", "   3", "   4", "   5", "   6", "   7")
                    break
                elif sutun_satir_dolumu == 0 :
                    print("---\nGirdiğiniz Sutun Bos Lütfen Farklı Bir Sutun Deneyiniz\n---")
            elif kullanici_girisi_sutun != int(kullanici_girisi_sutun):
                print("Lütfen Bir Tamsayı Giriniz")
                continue
            elif int(kullanici_girisi_sutun)<1 or int(kullanici_girisi_sutun)>7:
                print("Lütfen 0 ile 8 arasında bir sutun numarasi giriniz\n-")
                continue
        elif int(kullanici_girisi) == 1 or int(kullanici_girisi) == 2:
            print("Lütfen Seçiminizi Tamsayı Olarak Giriniz\n---")
        else :
            print("Lütfen Geçerli Bir Tamsayı Giriniz\n---")