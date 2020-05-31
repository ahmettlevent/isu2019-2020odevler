from bs4 import BeautifulSoup

import myurllib2


class IstinyeDersAnaliz():
    def __init__(self):
        self.department_names_dic = {"bm": "bilgisayar-muhendisligi", "eem": "elektrik-elektronik-muhendisligi",
                                     "mm": "makine-muhendisligi", "im": "insaat-muhendisligi",
                                     "em": "endustri-ve-sistem-muhendisligi",
                                     "ym": "yazilim-muhendisligi"}
        self.show_data_matrix()

    def show_data_matrix(self,):
        ''' Bu fonksiyon benzlerlik ölçütü ve dersleri UI'den alip gerekli fonksiyonların çağırılmasından sorumludur'''
        lessons = ["bm", "mm"]  # Geçici bölüm listesi
        all_lessons = {}
        for i in lessons:
            lessonpage = self.get_page(i)
            lessons_dic = self.get_lesson_content(lessonpage)
            for i in lessons_dic:
                all_lessons[i] = {"name": lessons_dic[i]["name"], "content": lessons_dic[i]["content"]}
        rownames, colnames, data = self.make_data(all_lessons)

    def get_page(self, bolumadi):
        url = "https://muhendislik.istinye.edu.tr/tr/bolumler/{}/ders-icerikleri".format(
            self.department_names_dic[bolumadi])
        response = myurllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        lesson_url = soup("iframe")[0].extract()["src"]
        return lesson_url

    def get_lesson_content(self, lesson_url):
        import re
        lesson_dic = {}
        url = lesson_url
        response = myurllib2.urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        print(soup)
        for i in soup.find_all(attrs={"class": "derscontainer"}):
            if len(i("td")[10].text) > 0:  # Bu bölüm için içerik varmı kontrolü
                raw_lesson_code = i("td")[5].text
                raw_name = i("td")[6].text
                raw_content = i("td")[10].text
                re.sub(r'\r\n', '', raw_content)
                lesson_dic[raw_lesson_code] = {"name": raw_name, "content": raw_content}
                print(lesson_dic[raw_lesson_code] )
        return lesson_dic

    def make_data(self, lessons_dic):
        rownames, colnames, data = [], [], []
        for i in lessons_dic:
            rownames.append(i)
            line = lessons_dic[i]["content"]
            colnames.append(line)
        return rownames, colnames, data

if __name__ == '__main__':
    IstinyeAnaliz = IstinyeDersAnaliz()
