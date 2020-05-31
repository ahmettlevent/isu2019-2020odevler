import recommendations as rcm


def loadMovieGenre(data):
    veri = open(data).readlines()
    genres = ["Unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama",
              "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    prefs = dict()
    for satir in veri:
        film_verileri = satir.split("|")
        film_adi = film_verileri[1]
        ptr = 5
        prefs.setdefault(film_adi, dict())
        for gen in genres:
            if film_verileri[ptr] == "1":
                prefs[film_adi][gen] = 1
            ptr += 1
    return prefs


def main():
    sozluk = loadMovieGenre("imdb.txt")
    print(sozluk)
    print()
    tersyuzsozluk = rcm.transformPrefs(sozluk)
    print(tersyuzsozluk)
    print()
    filmler = ["Toy Story (1995)", "Free Willy (1993)", "Phenomenon (1996)"]
    pointer = 0
    for film in filmler:
        benzer = rcm.topMatches(sozluk, film, n=5, similarity=rcm.sim_jaccard)
        print(filmler[pointer], " için öneriler -->", [tup[1] for tup in benzer])
        pointer += 1
    print()
    pointer = 0
    turler = ['Adventure', 'Drama', 'Thriller']
    for tur in turler:
        benzer = rcm.topMatches(tersyuzsozluk, tur, n=5, similarity=rcm.sim_jaccard)
        print(turler[pointer], " için öneriler -->", [tup[1] for tup in benzer])
        pointer += 1


if __name__ == '__main__':
    main()
