#SORU 1
#elma,armut,muz,kivi,karpuz,kavun,nar
manav_listesi = [{'cins': 'elma', 'miktar':400}, {'cins':'kavun','miktar':91},{'cins': 'armut', 'miktar':250},{'cins':'kivi','miktar':115},{'cins':'karpuz','miktar':52},
{'cins': 'muz', 'miktar':900}, {'cins': 'armut', 'miktar':240},{'cins':'elma','miktar':150},{'cins':'muz','miktar':150},
{'cins':'kivi','miktar':153},{'cins':'karpuz','miktar':25},{'cins':'kavun','miktar':9},{'cins':'nar','miktar':550}, {'cins':'kavun','miktar':91}]
manav_yeni ={}
for i in manav_listesi:
    for a in manav_listesi:
         if i['cins'] == a['cins'] and i != a:
             yeni_miktar = i['miktar'] + a['miktar']
             manav_yeni[i['cins']] = yeni_miktar
         else :
             continue
print("----------------\n",manav_yeni,"\n----------------")


#SORU 2
zar_listesi =[{},{},{1,1},{(1,2),(2,1)},{(1,3),(2,2),(3,1)},{(1,4),(2,3),(3,2),(4,1)},{(1,5),(2,4),(3,3),(4,2),(5,1)},{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)},
              {(6,2),(5,3),(4,4),(3,5),(2,6)},{(3,6),(4,5),(5,4),(6,3)},{(6,4),(5,5),(4,6)},{(6,5),(5,6)},{(6,6)}]
while True:
    ilk_zar = int(input("Lütfen ilk zarın değerini giriniz\n"))
    ikinci_zar = int(input("Lütfen ikinci zarın değerini giriniz\n"))
    for i in range(len(zar_listesi)):
        if ilk_zar + ikinci_zar == i:
            print("{} ve {} değerleri için zarların gelme durumları şu şekildedir {}".format(ilk_zar,ikinci_zar,zar_listesi[i]))
    cikis = int(input("1.Devam\n2.Cikis\n"))
    if cikis == 1:
        continue
    elif cikis == 2:
        exit()

