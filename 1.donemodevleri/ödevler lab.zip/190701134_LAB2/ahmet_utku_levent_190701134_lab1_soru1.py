print("A şıkkı")#                A. Yaşları sırasıyla 25 ve 21 olan iki kişinin yaşları arasındaki fark.
Berk,Mert = 25,21                     # Berk in yaşı 25 ve Mertin yaşını 21 olarak farklı değişkenlere atadım.
yaslarin_farki = Berk - Mert          # Yapılan işlemi tek bir değişkene atadım.
print("Berk ile Mertin yaşları farkı {}.".format(yaslarin_farki)) # Ve değişkeni ekrana bastım.



print("\nB şıkkı")#  Üçü de float cinsiden olan şu üç değerin toplam değeri. ""  14.99, 27.95, ve 19.83  ""
float_toplam = 14.99+27.95+19.83        # Float tipindeki sayıların toplamlarını tek bir değişkene atadım.
print("Float tipindeki değerlerin toplamları {}.".format(float_toplam))#Print komutu ile ekrana bastım.



print("\nC şıkkı")#              C. Uzunluğu 20 genişliği 15 birim olan bir dikdörtgenin alanı
dikdortgen_kısa_kenar,dikdortgen_uzun_kenar = 15,20     # Dikdörtgenin kısa ve uzun kenarını ayrı değişkenlere atadım.
dikdortgen_alani = dikdortgen_kısa_kenar*dikdortgen_uzun_kenar # Dikdörtgenin alanını buldum ve bir değişkene atadım
print("Dikdörtgenin alanı {} metredir.".format(dikdortgen_alani))# Dikdörtgenin alanını print komutu ile ekrana bastım.



print("\nD şıkkı")#              D. 2’nin 10. Kuvveti.
print("İkinin onuncu kuvveti {}.".format(2**10))   # İkinin onuncu kuvvetini hesaplatıp print komutu ile ekrana bastım.



print("\nE şıkkı")#              E. "" 3, 1, 8, -­2, 5, ­‐3, 0 "" Sayılarının değer olarak en küçüğünü veren ifade.
sayi_listesi = [3,1,8,--2,5,--3,0]          # Verilen sayılar ile bir liste oluşturdum.
print("Listedeki en küçük değer {} ".format(min(sayi_listesi)))
# Listedeki en küçük değeri min() metoduyla bulup değeri print ettim.


print("\nF şıkkı")#              F.17’nin 5’e tamsayı olarak bölümünün 3’e eşit olduğunun teyidi.
bolme_islemi = int(17/5) # 17 değerini 5 e bölüp sonucu int() metoduyla tamsayıya çevirdim ve bunu bir değişkene atadım.
if bolme_islemi == 3:       # Sonucun 3 e eşit olup olmadığını if , else ile teyit edip sonucu ekrana bastım..
    print("17 sayısının 5 e tamsayı olarak bölümü 3'e eşittir.")
else:
    print("17 sayısının 5 e tamsayı olarak bölümü 3'e eşit değildir.")



print("\nG şıkkı")#              G.17’yi 5’e tamsayı olarak bölünce kalanın 3 olup olmadığının görülmesi.
bolme_isleminde_kalan = int(17 % 5)       # 17 değerinin 5 ten kalanını tamsayı tipinde bulup bunu bir değişkene atadım.
print(bolme_isleminde_kalan == 3)        # w.




print("\nH şıkkı")#              H.284’ün çift bir sayı olduğunun teyidi.
cift_sayi = 284%2       # 284 sayısının ikiden kalanını bulup bunu bir değişkene atadım.
print(cift_sayi == 0)
# Atadığım bu değişkenin 0'a eşitliğini sorguladım , eğer bu sayının 2 ye bölümünden kalanı 0 ise bu sayı çift dir.
#Sayı eğer çift ise ekrana True , değil ise False değerli basılacaktır.



print("\nİ şıkkı")#              İ.284’ün hem çift sayı hem de 3’e tam bölünebilen bir sayı olup olmadığının görülmesi.
a,b = 284%2,284%3           # 284 sayısının ikiye ve üçe bölümünden kalanlarını farklı değişkenlere atadım.
print(a == 0 and b == 0 )          # Bu değişkenlerin verilen rakamlara tam bölünüp bölünmediği sorguladım .
# Sonucun False olması bize 284 sayısının hem çift hemde 3 e bölünebilen bir sayı olmadığını gösteriyor.



print("\nJ şıkkı")#              J.284’ün çift sayı ya da 3’e tam bölünebilen bir sayı olup olmadığının görülmesi.
a,b = 284%2,284%3           # 284 sayısının ikiye ve üçe bölümünden kalanlarını farklı değişkenlere atadım.
print(a == 0 or b == 0)           # Bu değişkenlerin verilen rakamlara tam bölünüp bölünmediği sorguladım .
# Sonucun True olması bize 284 sayısının çift veya 3 e bölünebilen bir sayı olduğunu gösteriyor.


