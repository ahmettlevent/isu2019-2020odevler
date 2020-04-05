import recommendations
class JaccardCalc():
    def __init__(self):
        self.TurAdlari = ["unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
                          "Drama",
                          "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller",
                          "War", "Western"]
        self.filmadlari = set()
        self.turler = set()

        self.data = self.getDATA()
        self.data[1681] = self.data[1681][:-1]  # Son satırdaki \n silinmesi için yazılmıştır

    def getDATA(self):
        # Eger veri aynı dizinde bulunuyorsa open ile açılacaktır aksi takdirde html sayfasından çekilecektir.
        try:
            file = open("u.item.txt", "r", encoding="utf-8")
            return file.read()
        except:
            import urllib.request
            page = urllib.request.urlopen("http://files.grouplens.org/datasets/movielens/ml-100k/u.item").read()
            page = str(page)[2:-2].split(r"\n")
            return page

    def critics(self):
        sahipolduguTurler = {}  # Her Bir Filmin ayri ayri sahip oldugu turleri dondurmek icin surekli bir degiskendir.
        criticsDic = {}
        for i in self.data:
            i = i.split("|")
            self.filmadlari.add(i[1])
            for c in range(19):
                if i[5 + c] == "1":
                    sahipolduguTurler[self.TurAdlari[c]] = 1
            criticsDic[i[1]] = sahipolduguTurler
            sahipolduguTurler = {}
        return criticsDic

    def tersYuzCritics(self):
        return recommendations.transformPrefs(self.critics())


    def simJaccard(self):
        #return recommendations.sim_jaccard(self.tersYuzCritics(),"Action","Adventure")
        print(self.critics())
        print(recommendations.topMatches(self.critics(), "Toy Story (1995)"))
        print(recommendations.topMatches(self.critics(), "Free Willy (1993)"))
        print(recommendations.topMatches(self.critics(), "Phenomenon (1996)"))

        print(recommendations.getRecommendations(self.critics(), "Toy Story (1995)", recommendations.sim_jaccard))
        print(recommendations.getRecommendations(self.critics(), "Free Willy (1993)", recommendations.sim_jaccard))
        print(recommendations.getRecommendations(self.critics(), "Phenomenon (1996)", recommendations.sim_jaccard))
    def topMatches(self):
        return recommendations.topMatches(self.critics(),"Free Willy (1993)")



movie_like = JaccardCalc()
#print(movie_like.critics())
print(movie_like.simJaccard())
#print(movie_like.tersYuzCritics())