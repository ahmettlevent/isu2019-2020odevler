## SORU -----1
asal_sayi_listesi = []
asal_sayi_sayisi = 0 # Üstte oluşturduğum listede 10 adet asal sayı birikirken bunu sayması için bir değişken tanımlıyorum
for i in range(2, 230):
    for a in range(2, i): # 2 ile sıradaki i sayısı arasındaki sayılar sırasıyla a değişkenine tanımlanıyor ve if bloğu bölünebilirliğini test ediyor
        if (i % a) == 0:
            break
    else:
        asal_sayi_sayisi += 1 # Her bir asal sayıda sayaç bir artıyor.
        asal_sayi_listesi.append(i) # Asal sayı Oluşturulan listeye eklendi.
        if asal_sayi_sayisi == 10:
            print(asal_sayi_listesi)
            asal_sayi_listesi = [] # 10 adet asal sayı biriktiği ve ekrana basıldığı için listeyi ve sayacı temizliyorum
            asal_sayi_sayisi -= 10

## SORU -----2
# Hilbert Eğrisi
import turtle
ceg = turtle.Turtle()
ceg.speed(0)
ceg.lt(90) # EĞRİNİN  KOORDİNAT DÜZLEMİNDE Y DOĞRUSUNDA PARALEL OLARAK ÇİZİLMESİ İÇİN TURTLE 90 DERECE SOLA DÖNDÜRÜLMÜŞTÜR
def hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece , ilk_adim_yonu):
    if derece < 1:
        return
    if ilk_adim_yonu== True :
        turtle.lt(90)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece -1, False)
        turtle.fd(kenar_uzunlugu)
        turtle.rt(90)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece -1, True)
        turtle.fd(kenar_uzunlugu)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece -1, True)
        turtle.rt(90)
        turtle.fd(kenar_uzunlugu)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece -1, False)
        turtle.lt(90)
    if ilk_adim_yonu == False:
        turtle.rt(90)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece - 1, True)
        turtle.fd(kenar_uzunlugu)
        turtle.lt(90)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece - 1, False)
        turtle.fd(kenar_uzunlugu)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece - 1, False)
        turtle.lt(90)
        turtle.fd(kenar_uzunlugu)
        hilbert_egrisi_ciz(turtle, kenar_uzunlugu, derece - 1, True)
        turtle.rt(90)
#------------------------------------------------------------------------
hilbert_egrisi_ciz(ceg, 15, 4, False)
turtle.done()
'''
Yukarıdaki Fonksiyonda  "ceg" turtle adını , "10" bir kenar uzunluğunu , "4" hilbert eğrisinin derecesini belirtir.
Son Parametre olan "True" yerine ise "True" yazılır ise ilk adım yönü sol , "False" yazılır ise ilk adım yönü sağ olur.
                                   

'''

