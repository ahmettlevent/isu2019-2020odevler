s1,s2,s3 = ("iyi"),("kotu"),("cirkin")

print("a. “rk”nin s3’in içinde mevcut olup olmadığı.")
print("rk" in s3) # "rk" string'ini s3 ün içerisinde arattım.Sonucun True çıkması s3'ün içinde bulunduğunu gösteriyor.

print("\nb. Boşluk karakterinin s1’in içinde olmadığının görülmesi.")
print(" " in s1) # Boşluk karakterini s1 in içinde arattım.Sonucun False olması s1'de bulunmadığını gösterecektir.

print("\nc. s1, s2 ve s3 arka arkaya eklendiğinde elde edilen sonuç.")
print(s1+s2+s3) # s1 s2 ve s3 ü arka arkaya toplayıp sonucu ekrana bastırdım.

print("\nd. Boşluk karakterinin s1, s2 ve s3 arka arkaya eklendiğinde ortaya çıkan sonuçta olup olmadığının görülmesi.")
degerlerin_toplami = (s1+s2+s3) # s1 , s2 ve s3 stringlerinin toplamını bir değişkene atadım.
print(" " in degerlerin_toplami)# Bu değişken içerisinde boşluk karakterini arattım , False durumu olmadığını belirtti.

print("\ne. s3'ün 10 ke arka arkaya eklemlenmiş halinin bir operasyonla elde edilmesi.")
print(s3*10)#s3 ün 10 kere arka arkaya eklenmesi 10 ile çarpılmasına eşittir,10 ile çarpıp sonucu ekrana bastım.

print("\nf. s1, s2 ve s3 arka arkaya eklendiğinde ortaya çıkan sonucun kaç karakter uzunluğunda olduğunun bulunması.")
print(len(s1+s2+s3)) # s1,s2,s3 stringlerini toplayıp "len()" metoduyla oluşan yeni stringin uzunluğunu buldum.