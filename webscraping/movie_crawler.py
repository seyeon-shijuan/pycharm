import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200916'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
imax = soup.select_one('span.imax')
if(imax):
    imax=imax.find_parent('div',class_='col-times')
    title=imax.select_one('div.info-movie > a > strong').text.strip()
    print(title,'Imax 예매가 열렸습니다.')
else:
    print('Imax 예매가 없습니다.')