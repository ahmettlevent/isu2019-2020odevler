import turtle

#1.SORU POLYGON FONKSİYONU

def polygon(ceg,kenar_uzunluk,kenar_sayisi):
    ceg = turtle.Turtle()
    ceg.rt(135)
    ceg.penup()
    ceg.fd(200)
    ceg.lt(135)
    ceg.pendown()
    print(ceg)
    a = 360/kenar_sayisi
    ceg.rt(a)
    kenar_uzunluk *= 10   # GÖRÜNTÜNÜN DAHA NET GÖZÜKMESİ İÇİN UZUNLUĞU 10 İLE ÇARPIYORUM
    for i in range(kenar_sayisi):
        ceg.fd(kenar_uzunluk)
        ceg.lt(a)
    print(ceg)
    ceg.lt(a)
    ceg.penup()
    ceg.fd(175)
    ceg.pendown()
    turtle.mainloop()


#2.SORU CİRCLE FONKSİYONU

def circle (a,r):
    polygon(a,r/2,r**2) # kenar sayısı girilen kenar sayısının karesi olarak alınmış ve uzunluk kenar sayısının yarısı kadar belirlenmiştir.




giris = int(input("Lütfen Bir Soru Seçiniz  '1 veya 2'   ('int' tipinde)  (Arkaplanda Çalışmaya Başlayacaktır..) "))
if giris == 1:
    y = int(4) # BİR KENARININ UZUNLUĞU 4 CM OLAN ÇOKGEN
    z = int(9) # BU ÇOKGENİN KENAR SAYISI 5
    a = "ahmet"
    print("{} köşeli bir çokgen oluşturulmuştur.".format(z))
    polygon(a, y, z)
elif giris == 2 :
    a = "ahmet"
    cemberpurussuzlugu = 6  #  SORU 2 İÇİN ÇEMBER BÜYÜKLÜĞÜ VE PÜRÜSSÜZLÜĞÜ ( KENAR SAYISI )
    circle(a,cemberpurussuzlugu)