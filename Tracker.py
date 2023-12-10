from importlib.resources import contents
from lib2to3.pgen2 import driver
from pydoc import describe
from turtle import title
import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium.webdriver.common.by import By


webhook_url = 'https://discord.com/api/webhooks/973857811928850442/l65X6LieJI5dpSGQ7FfvO1LiGyU6I7C4yplf0'
webhook = DiscordWebhook(
    url=webhook_url, content="The connection is successful")
response = webhook.execute()

opts = Options()
driver = webdriver.Chrome(options=opts)
hedef_url1 = "https://www.vatanbilgisayar.com/sony-playstation-5-digital-surum-oyun-konsolu.html"
hedef_url2 = "https://www.vatanbilgisayar.com/microsoft-xbox-series-s-oyun-konsolu.html"
hedef_1 = [hedef_url1, 0, 0]
hedef_2 = [hedef_url2, 0, 0]
dongusayisi = 0


def stokKontrol(hedef):
    global dongusayisi
    a = dongusayisi
    a += 1
    dongusayisi = a
    print(("Döngü= "+str(a)))
    driver.get(hedef[0])
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    butonlar = soup.find(
        "button", {"class": "btn-success"})
    urun_ismi = soup.find("h1", {"class": "product-list__product-name"})
    for x in range(1):
        if "Sepete Ekle" in butonlar.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(
                    url=webhook_url, content='In Stocks= '+hedef[0])
                urun_ismi = 'VATAN' + str(urun_ismi.text) + 'In Stocks'
                embed = DiscordEmbed(title=urun_ismi, deseription=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print("! ! ! In Stocks ! ! !" + str(urun_ismi))
                hedef[1] = hedef[2]
        else:
            hedef[1] = 0
            print(str(urun_ismi.text)+'Urun Stoklarda yok')
        print(hedef[0])


while True:
    stokKontrol(hedef_1)
    time.sleep(20)
    stokKontrol(hedef_2)
    time.sleep(20)
