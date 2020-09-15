#pip install python-telegram-bot
import requests
import telegram
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup
#from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200916'



my_token = ''
my = telegram.Bot(token = my_token)
updates = my.getUpdates()
for u in updates:
    print(u.message)


def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=1111111111, text=title + 'imax 예매가 열렸습니다')
        sched.pause()
        # print(title,'Imax 예매가 열렸습니다.')

'''
sched = BlockingScheduler()
sched.add_job(job_function(),'interval',seconds=30)
sched.start()
'''

sched = BackgroundScheduler()

sched.start()

sched.add_job(job_function(), 'interval', seconds=30)


'''
필기
pip install bs4 requests
crawling_first

iframe이있으면 기본 도메인에
/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200914
만붙이면 그 부분만 가져올 수 있다.

date=20200914 이 부분이 날짜이기 때문에 수정할 수 있다.
쿼리스트링을 잘 파악하면된다.

bs4 BeautifulSoup에는 find랑 select가 있다.

개발자도구에서 필요한 태그를 오른쪽눌러서 copy - copy selctor하면 필요한 부분만 복사해올 수 있다.
body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong
이렇게

select한 것을 for문으로 돌려서 1개 1개 태그를 부를거면
select_one을 하면 된다.

find_parent('div',class_='col-times')하면 부모태그로 이동할 수 있다.

pip install python-telegram-bot

AWS에서
EC2를 검색한다.

ubuntu 16선택
t2.micro선택
서버시작하기 (아래)
ssh -i 이름.pem ubuntu@awsip주소

sudo apt-get update
sudo apt-get install python3-pip
pip3 install requests bs4 python-telegram-bot apscheduler


ls movie_crawler.py
있는지 여부 확인

python3 movie_crawler.py
하면 실행됨

no hub으로 실행시키면 background로 실행가능함

nohup python3 movie_crawler.py &

실행중인 프로세스종료방법(아래)
ps -ef
kill
'''