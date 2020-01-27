import math
############ Soru 1
print("----------SORU 1----------")

def kucuksayifonk(n1, n2):
    sayiliste = [n1,n2]
    print("Küçük Sayı '{}' dir.Büyük Sayı '{}' dir.".format(min(sayiliste),max(sayiliste)))
    return min(sayiliste)
a = int(input("Herhangi Bir Tamsayı Girin\n"))
b = int(input("Herhangi Bir Tamsayı Girin\n"))
kucuk_sayi = kucuksayifonk(a,b)
print("{} sayısı geri çağırılmıştır.".format(kucuk_sayi))


############ Soru 2
print("----------SORU 2----------")

def oklidmesafesi(px, py, qx, qy): # P(px, py) ve Q(qx, qy)
    oklid_uzakligi = (((px-qx)**2) + ((py-qy)**2) )**(1/2)
    return oklid_uzakligi
print("(Px,Py) Noktası için")
px = int(input("Lütfen Px değerini girin\n"))
py = int(input("Lütfen Py değerini girin\n"))
print("(Qx,Qy) Noktası için")
qx = int(input("Lütfen Qx değerini girin\n"))
qy = int(input("Lütfen Qy değerini girin\n"))
print("Verilen noktalar arası öklid uzaklığı {} olarak hesaplanmıştır.".format(abs(oklidmesafesi(px,py,qx,qy))))
