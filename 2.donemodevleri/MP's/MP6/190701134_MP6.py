from bs4 import BeautifulSoup

import myurllib2


class IstinyeDersAnaliz():
    def __init__(self):
        self.department_names_dic = {"bm": "bilgisayar-muhendisligi", "eem": "elektrik-elektronik-muhendisligi",
                                     "mm": "makine-muhendisligi", "im": "insaat-muhendisligi",
                                     "em": "endustri-ve-sistem-muhendisligi",
                                     "ym": "yazilim-muhendisligi"}
        self.show_data_matrix()

    def show_data_matrix(self):
        ''' Bu fonksiyon benzlerlik ölçütü ve dersleri UI'den alip gerekli fonksiyonların çağırılmasından sorumludur'''
        lessons = ["bm", "mm"]  # Geçici bölüm listesi

        all_lesson_details = self.all_lessons(lessons)

        rownames, colnames, data = self.cook_data(all_lesson_details)
        self.show_screen(rownames, colnames, data)

    ''' 1.Seviye Fonksiyonlar'''

    def all_lessons(self, lessons):
        # ready
        all_lessons = {}
        for i in lessons:
            lessonpage = self.get_page(i)
            lessons_dic = self.get_lesson_content(lessonpage)
            for i in lessons_dic:
                all_lessons[i] = {"code": lessons_dic[i]["code"], "name": lessons_dic[i]["name"],
                                  "content": lessons_dic[i]["content"]}
        return all_lessons

    def show_screen(self, rownames, colnames, data):
        print(colnames, end=" ")
        print("\n")
        for i in range(len(rownames)):
            print("")
            print(rownames[i], end=" ")
            print(len(data))
            for a in data[i]:
                print("" + str(a), end=" ")

    def cook_data(self, lessons_dic):
        rownames, colnames, data = [], [], []
        allwords = set()
        illegal_words = ["", " ", "."]  # Degerlendirme disi kelimeler
        for i in lessons_dic:
            # Ders isimleri listeye ekleniyor
            rownames.append(lessons_dic[i]["code"])

            # O kelimenin Histogram'ı Çıkarılıyor
            lessons_dic[i]["data"] = {}
            for a in lessons_dic[i]["content"].split(" "):

                try:
                    if a.strip() in illegal_words:
                        break
                    if lessons_dic[i]["data"][a.strip()]:
                        lessons_dic[i]["data"][a.strip()] += 1
                except KeyError:
                    allwords.add(a.strip())
                    lessons_dic[i]["data"][a.strip()] = 1

        # Histogramdan elde edilen veriler listelere atiliyor
        colnames = list(i for i in allwords)
        for i in lessons_dic:
            # eger ders icerisinde kelime var ise adedi yok ise degeri 0 veriliyor
            lesson_temp_list = []
            for a in colnames:
                try:
                    if lessons_dic[i]["data"][a]:
                        lesson_temp_list.append(lessons_dic[i]["data"][a])
                except:
                    lesson_temp_list.append(0)
            data.append(lesson_temp_list)

        return rownames, colnames, data

    ''' 1.Seviye Fonksiyonlarda Kullanılan Alt Fonksiyonlar '''

    def get_page(self, bolumadi):
        '''Verilen Url'de Bulunan Sayfayı geri döndürür'''
        url = "https://muhendislik.istinye.edu.tr/tr/bolumler/{}/ders-icerikleri".format(
            self.department_names_dic[bolumadi])
        response = myurllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        lesson_url = soup("iframe")[0].extract()["src"]
        return lesson_url

    def get_lesson_content(self, lesson_url):
        lesson_dic = {}
        url = lesson_url
        response = myurllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        for i in soup.find_all(attrs={"class": "derscontainer"}):
            if len(i("td")[10].text) > 0:  # Bu bölüm için içerik varmı kontrolü
                raw_lesson_code = i("td")[5].text
                raw_name = i("td")[6].text
                raw_content = i("td")[10].text
                lesson_dic[raw_lesson_code] = {"code": raw_lesson_code, "name": raw_name, "content": raw_content}
        return lesson_dic


if __name__ == '__main__':
    IstinyeAnaliz = IstinyeDersAnaliz()
