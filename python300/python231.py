#231
'''
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result) 이렇게 하면 함수가 끝나고 나서 result를 call 해봤자 메모리에 남은 것이 없다.
'''

#232
def make_url(url):
    return "www"+url+".com"

#233
def make_list(mystr):
    mylist=[]
    for i in mystr:
        mylist.append(mystr)
    return mylist
#str도 쪼갤 수있다.

def make_list (string) :
    return list(string)

#234
def pickup_even(mylist):
    returnlist=[]
    for i in mylist:
        if i%2==0: returnlist.append(i)
    return returnlist

#235
def convert_int (string) :
    return int(string.replace(',', ''))

#236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
#22

#237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)
#22

#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)
#140

#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
#16

#240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#28


