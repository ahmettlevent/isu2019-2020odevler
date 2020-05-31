from clusters import *


def show(blognames, data, jpeg_name):

    h_clust = hcluster(data)
    drawdendrogram(h_clust, blognames, jpeg=jpeg_name)

    k_clust = kcluster(data)
    for i in range(len(k_clust)):
        print([blognames[r] for r in k_clust[i]])


def main():

    # soru 1
    urls, labels, data = readfile('bookmark_data2.txt')
    show(urls, data, "h_clust1.jpg")

    # soru 2
    new_data = rotatematrix(data)
    show(labels, new_data, "h_clust2.jpg")


if __name__ == '__main__':
    main()

