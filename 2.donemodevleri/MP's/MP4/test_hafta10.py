import mysearchengine

pagelist=['http://istinye.info']

dbtables = {'urllist': 'urllist.db',
            'wordlocation':'wordlocation.db',
            'link':'link.db',
            'linkwords':'linkwords.db'}

crawler=mysearchengine.crawler(dbtables)
crawler.createindextables()
crawler.crawl(pagelist)
# Aşağıdaki close adımı önemli!
crawler.close()

input ("Crawling Bitti, searching için bir tuşa basın....")

searcher = mysearchengine.searcher(dbtables)
searcher.query('homework')
searcher.query('computer')
# Aşağıdaki close adımı önemli!
searcher.close()


# Bu noktada searcher sınıfı getscoredlist() fonksiyonundaki weights listesindeki dağılımları değiştirerek,
# ardından yeni bir searcher instance'i yaratıp, daha önce doldurulmuş olan index tabloları üzerinden, yeniden
# crawling (emekleme) yapmadan arama (query) yapabilir ve sonuçların nasıl değiştiğini gözlemleyebilrsiniz.
# Bunun için yukarıdaki bütün satırları comment-out edin ve aşağıdakileri açın.

# import mysearchengine
# searcher = mysearchengine.searcher(dbtables)
# searcher.query('homework')
# searcher.query('computer')
# # Aşağıdaki close adımı önemli
# searcher.close()



















#searcher.query(u'şehir üniversitesi')
