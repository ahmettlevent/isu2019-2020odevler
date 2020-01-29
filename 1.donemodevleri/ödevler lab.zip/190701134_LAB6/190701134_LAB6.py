import time
print("------SORU 1------")
# SORU 1

def ussuMU(x, y):
    global n
    if x%y != 0:
        return False
    elif y > x :
        return False
    elif x%y_main == 0 and x/y_main == y_main**n:
        return True
    else:
        n+=1
        return ussuMU(x,y_main**n)
n = 0
x_main,y_main=144,12 #x_main , y_main 'in üssüdür veya değildir olarak düşünülmüştür. ve programa tanıtılmıştır.
print(ussuMU(x_main,y_main)) # x_main sayısı ulaşılmak istenen sayıdır , y_main sayısı üssü alınacak olan sayıdır.
#------------------------------------------------------------------------------------------------------------------------------------------------------------
time.sleep(1)
print("------SORU 2------")

def recurse(n, s):
    '''
    recurse(n,s)
        Bu fonksiyona girilen 'n' parametresi eğer int(0) olur ise 's' parametresini ekrana basacaktır.
        Eğer 'n' değeri int(0) değil ise program else bloğuna geçecek ve özyineleme yaparak
        girilen 'n' değerini 1 eksiltecek ,
        's' değerini 'n' ile toplayacaktır ve bunu kendine('s') eşitleyecektir.
        Bu döngü n değeri int(0) olana kadar çalışacaktır.

    recurse(3,0):
        Bu durumda program 3 kez else bloğunu çalıştıracaktır ve bu sırada her seferinde
        'n' değeri 1 eksiltilecek
        's' değeri ise o anki 'n' değeri ile toplanacaktır
        Program sonunda 's' değeri '6' olarak ekrana basılacaktır
    recurse(-1,0)
        Bu durumda 'n' değeri 0 dan küçük ve eşit olmadığı için sürekli recurse edilecek ve her seferinde '1' eksileceği için
        program sonsuz kez çalışacaktır.
        Bu sırada 's' değeride sürekli olarak 'n' ile toplanacak ve eksi sonsuza doğru gidecektir.
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
print(recurse.__doc__)