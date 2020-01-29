from concord import concord_hesapla

#------------------------------METINLER------------------------------------

with open("ingilizce_text_metin.txt","r") as metin_ingilizce:
    metin_ingilizce_list = []
    for i in metin_ingilizce:
        metin_ingilizce_list.append(i[:-1])
with open("turkce_text_metin.txt","r") as metin_turkce:
    metin_turkce_list = []
    for i in metin_turkce:
        metin_turkce_list.append(i[:-1])

#------------------------------STOPWORDLER---------------------------------

with open("turkish_stop_words.txt","r") as stopword_turkce:
    stopword_turkce_list = []
    for i in stopword_turkce:
        stopword_turkce_list.append(i[:-1])
with open("english.stop_words.txt","r") as stopword_ingilizce:
    stopword_ingilizce_list = []
    for i in stopword_ingilizce:
        stopword_ingilizce_list.append(i[:-1])

# ----------------------------------MENU-----------------------------------

while True:
    global concordance
    dil_secim = int(input("--Dil Secim Ekrani--\n1.Ingilizce metin\n2.Turkce metin\n"))

    if dil_secim == 1:
        concordance = concord_hesapla(metin_ingilizce_list,stopword_ingilizce_list)

    elif dil_secim == 2:
        concordance = concord_hesapla(metin_turkce_list,stopword_turkce_list)

    else :
        print("\n--\nLutfen 1 veya 2 giriniz\n--\n")
        continue
    for kelime in concordance:
        print(kelime, ": Toplam Sayi: {}".format(concordance[kelime][0]))
        for satir_no in range(concordance[kelime][0]):
            print("Satir : {} {}".format(concordance[kelime][1][satir_no][0], concordance[kelime][1][satir_no][1]))
        print()
