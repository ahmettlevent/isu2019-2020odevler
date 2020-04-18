from clusters import *

##############################################

(Urls, word, data) = readfile("bookmarkdataset2.txt")

clust = hcluster(data)
drawdendrogram(clust, Urls, jpeg='hclust-urls')

kclust = kcluster(data, k=5)

print([Urls[r] for r in kclust[0]])
print([Urls[r] for r in kclust[1]])

#################################################

(word2, Urls2, data2) = readfile("bookmarkdataset.txt")

clust2 = hcluster(data2)
drawdendrogram(clust2, word2, jpeg='hclust-words')

kclust2 = kcluster(data2, k=5)

print([word2[r] for r in kclust2[0]])
print([word2[r] for r in kclust2[1]])


def ahmet():
    pass
ahmet()