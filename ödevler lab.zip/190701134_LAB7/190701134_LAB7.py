a_listesi = []
b_listesi = []
c_listesi = []
d_listesi = []
for a in range(4,9,1):
    a += 1
    a_listesi.append(a)
print("a şıkkı şu şekildedir = {}".format(a_listesi))
for b in range(4,25,5):
    b += 1
    b_listesi.append(b)
print("b şıkkı şu şekildedir = {}".format(b_listesi))
for c in range(29,3,-5):
    c += 1
    c_listesi.append(c)
print("c şıkkı şu şekildedir = {}".format(c_listesi))
for d in range(1,68,13):
    d += 1
    d_listesi.append(d)
print("d şıkkı şu şekildedir = {}".format(d_listesi))

for i in range(0,8,1):
    print((8-i)*" ",i*"+")
for i in range(8,0,-1):
    print((8-i)*" ",i*"+")

