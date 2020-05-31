import urllib.request
from bs4 import BeautifulSoup
url = "https://www.n11.com/urun/vestel-40f9400-40-full-hd-smart-led-tv-1173803?magaza=doludepo"
response = urllib.request.urlopen(url=url)
soup = BeautifulSoup(response.read(), features="html.parser")
page = soup.find("section", {"class": "uni-content"})
