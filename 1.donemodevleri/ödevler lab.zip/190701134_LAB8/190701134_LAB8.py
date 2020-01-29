# SORU 1

istenmeyen_karakter ="!,',^,+,%,&,/,(,),[,],{,},é,=,?,*,>,<,|,$,ç,ı,ü,ğ,ö,ş,İ,Ğ,Ü,Ö,Ş,Ç, ,"
istenen_karakter ="ABCDEFZHIKLMNOPQRSTVX,1,2,3,4,5,6,7,8,9,"
def identifier_check(a):
    if a[0] == "_" or a[0].isalpha() == True :
        for i in range(len(istenmeyen_karakter)):
            if (istenmeyen_karakter[i] in a) :
                return False
        for i in range(len(istenen_karakter)):
            if ( istenen_karakter[i] in a ) or ( istenen_karakter[i].lower() in a ) or ("_" in a):
                return True
    else:
        return False

kullanici_giris =str(input("Lütfen Bir String Giriniz"))
print(identifier_check(kullanici_giris))

#----------------------------------------

# SORU 2 

def duzenleyici_fonk(a):
    ilk_part_kelime = ""
    ikinci_part_kelime = ""
    a = a.replace(" ", "")
    for i in range(len(a)):
        if a[i] == a[i].upper():
            ikinci_part_kelime = ikinci_part_kelime + a[i]
        else:
            ilk_part_kelime = ilk_part_kelime +a[i]
    return ilk_part_kelime+ikinci_part_kelime
print(duzenleyici_fonk(str(input("Düzenlemek İstediğiniz Bir String Giriniz"))),end="")

#----------------------------------------