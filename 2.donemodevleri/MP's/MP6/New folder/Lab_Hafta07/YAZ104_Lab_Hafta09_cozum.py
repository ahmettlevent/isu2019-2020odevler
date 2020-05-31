import re
from bs4 import BeautifulSoup
import urllib.request as urllib2


def redesign(string):
    patern = '(\w+)?-(\w+)?'
    variables = string.split()
    newString = ""
    for variable in variables:
        status = re.search(patern, variable)
        if status is not None:
            if status.group(2) is None:
                variable = re.sub('-', '', variable)
            else:
                variable = re.sub('-[a-z]', status.group(2)[0].upper(), variable)
        newString += variable + ' '
    return newString


def make_soup(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), 'html.parser')
    return soup


def get_news(soup):
    dictionary = dict()
    data = soup.find("div", {"id": "data-block"})

    for news in data.findAll("h2", {"class": "sfnewsTitle"}):
        link = news.find("a")['href']
        if link[0] == '/':
            link = "http://www.itu.edu.tr/itu-hakkinda" + news.find("a")['href']

        newsList = news.text.split('\n')
        dictionary[newsList[1]] = {'link': link, 'tarih': newsList[4].lstrip(), 'aciklama': newsList[6]}

    return dictionary


def print_news(dictionary):
    for key in dictionary.keys():
        print("Başlık: {}\nTarih: {}\nLink: {}\nAçıklama: {}\n".format(key, dictionary[key]["tarih"], dictionary[key]["link"], dictionary[key]["aciklama"]))


def main():
    # soru 1
    string = "first-example secondexample- -thirdexample forthexample"
    newString = redesign(string)
    print(newString)

    # soru 2
    url = "http://www.itu.edu.tr/itu-hakkinda/haberler"
    soup = make_soup(url)
    dictionary = get_news(soup)
    print_news(dictionary)


if __name__ == '__main__':
    main()
