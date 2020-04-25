import bs4
from urllib.request import urlopen

newsdict= dict()

sauce = urlopen("http://www.itu.edu.tr/itu-hakkinda/haberler")

soup = bs4.BeautifulSoup(sauce.read(),"html.parser")

haberler_bilgisi = soup.find_all("h2", { "class" : "sfnewsTitle" })
haber_detay = soup.find_all("div", { "class" : "sfnewsSummary" })

for i,a in zip(haberler_bilgisi,haber_detay):
    newsdict[i.a.text]={}
    newsdict[i.a.text]["link"]="http://www.itu.edu.tr"+i.a['href']
    newsdict[i.a.text]["tarih"]=(i.div.text).replace("\n","").strip()
    newsdict[i.a.text]["aciklama"]=a.text
print(newsdict)
