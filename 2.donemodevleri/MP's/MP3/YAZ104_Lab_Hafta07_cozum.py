# recommendation modulunden transformPrefs fonksiyonunu aliyoruz (2. sorudaki tersyuz islemi icin)
from recommendations import transformPrefs

# Veri seti dosyasindan okuyup sozlukk haline getirmek icin fonksiyon
def openFile(filename):
    dictionary = dict()
    with open(filename) as openfile:
        for line in openfile:
            line = line.split(",")
            # satir sonundaki newline'dan kurtulalim
            line[-1] = line[-1].strip()
            sliced_line = line[3:]
            for i in range(0, (len(sliced_line) - 1), 2):
                dictionary.setdefault(sliced_line[i], {})
                dictionary[sliced_line[i]][line[0]] = sliced_line[i + 1]

    return dictionary

# Sozlukten matris dosyasi olusturma.
def createMatrices(filename):
    datadictionary = openFile(filename)
    # Sozlugu ikinci sorudan once terzyuz etmek gerekiyor
    transposedDict = transformPrefs(datadictionary)
    # 1. soru için matris olusturma
    createMatrix(datadictionary, "bookmarkdataset.txt")
    # 2. soru icin matris olusturma
    createMatrix(transposedDict, "bookmarkdataset2.txt")


def createMatrix(datadictionary, out_file_name):
    out_file = open(out_file_name, "w")
    out_file.write("Tags")
    columnslist = []

    # create list of columns
    for value in datadictionary.values():
        for key in value:
            if key not in columnslist:
                columnslist.append(key)

    # write clolumns in columnlist to file
    for column in columnslist:
        out_file.write('\t%s' % column)
    out_file.write('\n')

    # convert dictionary to tuple list. The tuple is like that = [(tag,{url:value}]
    for key, value in datadictionary.items():
        out_file.write(key)
        out_file.write('\t')

        for column in columnslist:
            # if url not in values,it equalize it value to 0 and write to file
            if column not in value:
                out_file.write('0\t')
            else:
                out_file.write(value[column])
                out_file.write('\t')
        out_file.write('\n')


if __name__ == "__main__":
    createMatrices("delicious_data.txt")