def kup_fonk(a) : # x = küpün herhangi bir kenarının uzunluğudur.
    print("---\nBir kenarının uzunluğu {} cm olan küpün hacmi {} cm dir".format(a,a**3))
    return 6*a**2
def dikdortgenler_prizmasi_fonk(x,y,z): # dikdörtgenler prizmasının herhangi bir köşesindeki üç kenar uzunluğu = x,y,z
    print("---\nBir ayrıttaki üç kenarın uzunluğu {},{},{} olan dikdörtgenler prizmasının hacmi {} cm dir.".format(x,y,z,x*y*z))
    return 2*(x*y+x*z+y*z)
def piramit_fonk(x,z,h): # piramitin tabanındaki köşeler 'x' , 'y' ; piramitin yüksekliği ise 'h' dir.
    print("---\nBir ayrıttaki iki taban kenarı ve yüksekliği sırasıyla {},{},{} cm olan dörtgen piramitin hacmi {}cm dir.".format(x, z, h,((x*z)*h)/3))
    a = (((z/2)**2 + h**2)**(1/2))*x
    b = (((x/2)**2 + h**2)**(1/2))*z
    return (a+b+x*z)
def silindir(r,h,pi): # r = silindirin taban veya tavan yarıçapı , h = silindir yüksekliği , pi = pi sayısı
    print("---\nTaban yarıçapı {} cm ve yüksekliği {} cm olan silindirin hacmi {} cm dir.".format(r, h, pi*(r**2)*h))
    return (2*pi*r*h) + (2*pi*r**2)
def kure(r,pi): # r = kürenin yarıçapı , pi = pi değeri
    print("Yarıçapı {} cm olan bir kürenin hacmi {} cm dir.".format(r,(4*pi*r**3)/3))
    return (4)*pi*(r**2)



# == format modülünde
# 6 yerine yazacağınız değer küpün herhangi bir köşe uzunluğunu belirtir
print("Bu küpün yüzey alanı {} cm dir\n---".format(kup_fonk(6)))

# 3 , 4 , 5 yerine yazacağınız değer prizmanın herhangi bir ayrıtındaki üç farklı köşenin uzunluğunu belirtir
print("Bu dikdörtgenler prizmasının yüzey alanı {} cm dir.\n---".format(dikdortgenler_prizmasi_fonk(3,4,5)))

# 9 , 9 , 3 yerine yazacağınız değerler sırasıyla , 1 taban ayrıtındaki iki farklı veya aynı taban kenar uzunluğu,yükseklik
print("Bu piramitin yüzey alanı {} cm dir.\n---".format(piramit_fonk(9,9,3.1)))

# 4 , 3 , 3.14 yerine yazacağınız değerler sırasıyla silindirin , taban yarıçapı , yüksekliği , pi değeridir.
print("Bu silindirin yüzey alanı {} cm dir.\n---".format(silindir(4,3,3.14)))

# 2 , 3.14 yerine yazacağınız değerler sırasıyla kürenin yarıçapı , pi sayısı.
print("Bu kürenin yüzey alanı {} cm dir.\n---".format(kure(2,3.14)))

# FONKSİYONLARIN KULLANIMI !!
# print satırlarının üstünde yazılan değerlerden değişmek istediklerinizi .format içinde bulup değiştirmeniz yeterlidir.