#--SORU 1--------
def daireselMi(list1,list2):
    if len(list1)== len(list2):
        for i in list1:
            if list1 == list2:
                return True
            else:
                list1.reverse()
                list1.append(list1[0])
                list1.pop(0)
                list1.reverse()
        return False
    else:
        print("Liste Uzunlukları Eşit Değil !!")
        return False
liste_1 = ["C","E","G","I","D",26]
liste_2 = ["I","D",26,"C","E","G"]
print(liste_1)
print(liste_2)
print("+Dairesel mi ? \n-{}\n\n".format(daireselMi(liste_1,liste_2)))

#--SORU 2--------
def kume_fonk(x):
    kume = []
    for i in x:
        if i not in kume:
            kume.append(i)
        else:
            continue
    return kume
liste = ["yaz", 2, "103", 2, "program", 3, 5, "d", 0, "203", "program", 5, 5]
print(kume_fonk(liste))
