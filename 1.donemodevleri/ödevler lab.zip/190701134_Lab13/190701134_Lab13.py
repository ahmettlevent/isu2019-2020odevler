def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

#-----------------------------------------------------------

gutenberg_file = open("gutenberg_txt", "r", encoding="utf-8")
gutenber_tum_sozcukler = []
for i in gutenberg_file:
    for c in i[:-1].split():
        gutenber_tum_sozcukler.append(c)
#print(histogram(gutenber_tum_sozcukler))

#-----------------------------------------------------------

words_file = open("words.txt","r",encoding="utf-8")
words_tum_sozcukler = []
for i in words_file:
    for c in i[:-1].split():
        words_tum_sozcukler.append(c)
#print(histogram(words_tum_sozcukler))

#-----------------------------------------------------------


list = []
list_2 = []
sonuc_list = []
x = 0

for i in histogram(gutenber_tum_sozcukler).keys():
    list.append(i)

for i in histogram(words_tum_sozcukler).keys():
    list_2.append(i)
a = int(input("--\nwords dosyasında olmayıp gutenberg_txt dosyasında olan kelimeleri görmek için 1 i tuşlayın\nTam Tersi icin 2 yi tuslayin.\n"))
if a == 1 :
    for i in histogram(gutenber_tum_sozcukler).keys():
        if i.lower() in histogram(words_tum_sozcukler):
            continue
        else:
            print(i)
elif a == 2 :
    for i in histogram(gutenber_tum_sozcukler).keys():
        if i.lower() in histogram(words_tum_sozcukler):
            print(i)
        else:
            continue
print(histogram(gutenber_tum_sozcukler))