#011
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samelc=50000
totalvalue= samelc*10
print(totalvalue)

#012
시가총액=298000000000000
현재가=50000
PER = 15.79
print(시가총액,type(시가총액))
print(현재가,type(현재가))
print(PER,type(PER))

#013
s = "hello"
t = "python"
print(s,"!",t)

#014
print(2 + 2 * 3 ) #2+6=8

#015
a = "132"
print(type(a)) #<class 'str'> 따옴표안에있으면 String이다.

#016
num_str = "720"
num_str = int(num_str)
print(type(num_str)) #<class 'int'>

#017
#정수 100을 문자열 '100'으로 변환해보세요.
a=100
a = str(a)
print(type(a)) #<class 'str'>

#018
#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
a="15.79"
a=float(a)
print(type(a)) #<class 'float'>

#019
year = "2020"
year=int(year)
print(year-2,year-1,year) #2018 2019 2020

#020
#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
ppm=48584
tot=ppm*36
print(tot) #1749024
