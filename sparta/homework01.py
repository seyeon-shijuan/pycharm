from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=STC&q=%EC%9D%B4%EA%B0%80%EC%9D%80&period=6m&sd=20200401202758&ed=20201001202758") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
thumbnails = soup.select('#imgList > div > a > img')
i = 100
for thumbnail in thumbnails:
    img=thumbnail['src']
    print(img)
    dload.save(img,f'img/{i}.jpg')
    i+=1
###################################

driver.quit() # 끝나면 닫아주기