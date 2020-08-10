#031
a = "3"
b = "4"
print(a + b) #34
#따옴표 안 문자열이라서 붙이면 그냥 붙는다.

#032
print("Hi" * 3) #HiHiHi
#python의 장점임 문자열도 곱하면 그대로 x3됨

#033
print("-"*80)

#034
t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*4)

#035
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
#print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미

#036
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#037
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#038
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
print(상장주식수) #5969782550
상장주식수 = int(상장주식수)
print(type(상장주식수)) #<class 'int'>

#039
# '2020/03'만 출력
분기 = "2020/03(E) (IFRS연결)"
print(분기.split('(')[0]) #2020/03
#omg!! i'm so genius
print(분기[:7]) ##2020/03
#Slicing

#040
data = "   삼성전자    "
print(data.strip())
#java의 trim()이 python에서는 strip()이다.


