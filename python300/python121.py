#121
'''
user=input("입력:")
if user.islower():
    print(user.upper())
else: print(user.lower())
'''

#122
'''
user=input("입력:")
user=int(user)
if 81<=user<=100:
    print("A")
elif 61<=user<=80:
    print("B")
elif 41<=user<=60:
    print("C")
elif 21<=user<=40:
    print("D")
else: print("F")
'''

#123
'''
currencylist = {"달러":1167,
            "엔" : 1.096,
            "유로":1268,
            "위안":171
            }
user=input("입력:")
num, currency = user.split(" ")
print(float(num) * currencylist[currency],"원")
'''

#124
'''
x1=int(input("입력1:"))
x2=int(input("입력2:"))
x3=int(input("입력3:"))
if x1>x2:
    if x1>x3:print(x1)
    else: print(x3)
else: #x1<x2
    if x2>x3:print(x2)
    else: print(x3)
'''

#125
'''
telecom = {'011':'SKT',
           '016':'KT',
           '019':'LGU',
           '010':'알수없음'
           }
user=input("입력:").split("-")[0]
print(telecom[user],"고객입니다.")
'''

#126
'''
user=input("입력:")[:3]
if user in('010','011','012'):
    print("강북구")
elif user in('013','014','015'):
    print("도봉구")
else: print("노원구")
'''

#127
'''
user=input("입력:").split("-")[1]
if user[0]=="1" or user[0]=="3":
    print("남자")
else : print("여자")
'''

#128
'''
user=input("입력:").split("-")[1]
if 0<= int(user[1:3]) <=8:
    print("서울")
else: print("기타지역")
'''

#129
'''
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
'''

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#비트코인의 가격 정보를 딕셔너리로 가져오는 코드
변동폭 = float(btc['max_price'])-float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
# (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력
if(시가+변동폭) > 최고가:
    print("상승장")
else: print("하락장")