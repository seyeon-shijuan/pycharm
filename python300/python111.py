#111
#user=input("입력:") #shijuan
#print(user*2) #shijuanshijuan

#112
#user=input("입력:")
#print(int(user)+10) #int로 casting 필수

#113
'''
user=input("입력:")
if int(user)%2==0:
    print("짝수")
else: print("홀수")
'''

#114
'''
user=input("입력:")
if int(user)+20>255:
    print(255)
else: print(int(user)+20)
'''

#115
'''
user=input("입력:")
num=int(user)-20
if num>255:
    print(255)
elif num<0:
    print(0)
else:
    print(num)
'''

#116
'''
user=input("현재시간:")
if user[-2:] != "00":
    print("정각이 아닙니다.")
else : print("정각입니다.")
'''

#117
'''
fruit = ["사과", "포도", "홍시"]
user=input("입력:")
if user in fruit:
    print("정답입니다.")
else: print("오답입니다.")
'''

#118
'''
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user=input("입력:")
if user in warn_investment_list:
    print("투자경고리스트 입니다.")
else : print("정상")
'''

#119
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가 좋아하는 계절은:")
if user in fruit.keys():
    print("정답입니다.")
else : print("오답입니다.")
'''

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("내가 좋아하는 과일은:")
if user in fruit.values():
    print("정답입니다.")
else: print("오답입니다.")
