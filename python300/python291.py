#291
'''
f = open("C:/Users/-/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()
'''

#292
'''
f=open("C:/Users/-/Desktop/매수종목2.txt",mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()
'''

#293
'''
import csv

f = open("C:/Users/-/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()
'''

#294
'''
바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
f = open("C:/Users/-/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()   # python list

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)

f.close()
'''

#295
'''
#파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
f = open("C:/Users/-/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v

print(data)
f.close()
#{'005930': '삼성전자', '005380': '현대차', '035420': 'NAVER'}
'''

#296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

#297
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)

#298
try:
    b = 3 / 0
except ZeroDivisionError:
    print("ArithmeticException")

#299
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e) #printstacktrace

#300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data") #for문이라 try 정상 수행일 때마다 실행함
    finally:
        print("변환 완료")


#finished congrats ♥