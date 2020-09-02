#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
#안녕 Hi

#212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)
#7,15

#213
'''
def 함수(문자열) :
    print(문자열)
함수()
TypeError: 함수() missing 1 required positional argument: '문자열'
인 이유 = parameter가 필요한데 쓰지 않아서
'''

#214
'''
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
오류인 이유: 문자랑 숫자는 더할 수가 없어서
'''

#215
def print_with_smile(x):
    print(x+":D")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(x):
    print(x*1.3)

#218
def print_sum(x,y):
    print(x+y)

#219
def print_arithmetic_operation(x,y):
    print("{}+{}={}".format(x,y,x+y))
    print("{}-{}={}".format(x, y, x - y))
    print("{}*{}={}".format(x, y, x * y))
    print("{}/{}={}".format(x, y, x / y))

print_arithmetic_operation(1,2)

#220
def print_max(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else: print(z)

print_max(1,2,3)