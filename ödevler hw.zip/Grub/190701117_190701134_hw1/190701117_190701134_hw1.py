# 1.SORU TAM SAYININ MUTLAK DEĞERİNİ GERİ DÖNDÜREN BİR FONKSİYON
def ali_fonk (x):
    return x*((x>0)-(x<0))
mutlak1 = int((input("Lütfen Herhangi Bir Tamsayı Girin\n")))
print("Girdiğiniz Sayının Mutlak Değeri {} dir.".format(ali_fonk(mutlak1)))
# 2.SORU VERİLEN NOKTA ÇEMBERİN İÇİNDE Mİ ?
def ahmet_fonk (x, y, r):
    return (x**2+y**2) <= r**2
print("(5,5) noktasının 7 yarıçaplı çember içinde olması durumu {} dur".format(ahmet_fonk(5,5,7))) # False Çıkması Durumunda (5,5) Noktasının Çemberin İçinde Olmadığını Anlıyoruz
# 3.SORU TURTLE WORLD İLE WEEK YAZIMI
#input("TurtleWorld ile Week Yazım Kodunu Çalıştırmak için Herhangi Bir Tuşa Basın.\n")
print("Program Arkaplanda Çalışmaya Başlayacaktır.")
import turtle
ceg = turtle.Turtle()
ceg.rt(90)
ceg.fd(100)
ceg.lt(135)
ceg.fd(75)
ceg.rt(90)
ceg.fd(75)
ceg.lt(135)
ceg.fd(100)
ceg.penup()
ceg.rt(90)
ceg.fd(25)
ceg.pendown()
def gitgel():
    ceg.fd(75)
    ceg.rt(180)
    ceg.fd(75)
def birimasagi(x):
    ceg.lt(90)
    ceg.fd(x)
    ceg.lt(90)
for i in range(2):
    gitgel()
    birimasagi(50)
    gitgel()
    birimasagi(50)
    gitgel()
    ceg.penup()
    ceg.rt(90)
    ceg.fd(100)
    ceg.rt(90)
    ceg.fd(100)
    ceg.pendown()
ceg.rt(90)
ceg.fd(100)
ceg.rt(180)
ceg.fd(50)
ceg.rt(45)
caprazuzaklik = ((50*2+25*2)**1/2)
ceg.fd(caprazuzaklik)
ceg.rt(180)
ceg.fd(caprazuzaklik)
ceg.lt(90)
ceg.fd(caprazuzaklik)
print(ceg)
turtle.mainloop()