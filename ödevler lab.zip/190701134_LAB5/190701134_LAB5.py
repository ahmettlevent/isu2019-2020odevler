# SORU ----   1
kullanici_parasi = int(input("Vergi hesaplamak istediğiniz tutuarı girin."))
def Vergi_Hesap_Fonk(birinci_SINIR = 18000,ikinci_SINIR = 40000,ucuncu_SINIR = 148000):
    global giris_hakki
    giris_hakki = 1
    if kullanici_parasi >= 0 and kullanici_parasi <= birinci_SINIR :
        return kullanici_parasi*(15/100)
    elif kullanici_parasi >= birinci_SINIR and kullanici_parasi <= ikinci_SINIR :
        return kullanici_parasi*(20/100)
    elif kullanici_parasi >= ikinci_SINIR and kullanici_parasi <= ucuncu_SINIR :
        return kullanici_parasi*(27/100)
    elif kullanici_parasi >= ucuncu_SINIR:
        return kullanici_parasi*(35/100)
    else:
        print("Lütfen geçerli bir birim giriniz.")
        giris_hakki -= 1
Vergi_Hesap_Fonk()
if giris_hakki == 1 :
    print("{} TL Paranız için ödemeniz gereken vergi tutarı {} TL dir.".format(kullanici_parasi,Vergi_Hesap_Fonk()))



#----------------------------------------------------------------------------------------------------------------#


input("Devam etmek için enter tuşuna basın ")
# SORU -- 2
import turtle
ceg = turtle.Turtle()
def turtle_fonk(poly_kenaruzunluk,poly_kenarsayi):
    print(ceg)
    for i in range(poly_kenaruzunluk):
        while poly_kenaruzunluk >= 0:
            ceg.rt(15)
            for i in range(poly_kenarsayi):
                ceg.fd(poly_kenaruzunluk)
                ceg.rt(360/poly_kenarsayi)
            poly_kenaruzunluk -= 8
turtle_fonk(160,5)
turtle.done()

