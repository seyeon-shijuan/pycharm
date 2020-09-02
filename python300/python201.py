#201
def print_coin():
    print("비트코인")

#202
print_coin()

#203
for i in range(10):
    print_coin()

#204
def print_coins():
    for i in range(10):
        print("비트코인1")

#205
'''
hello()
def hello():
    print("Hi") 가 오류인 이유는 정의하기 전에 윗줄에서 없는 함수를 call해서
'''

#206
def message() :
    print("A")
    print("B")

message()
print("C")
message()

#207
print("A")

def message() :
    print("B")

print("C")
message()

#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
#ACBED

#209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
#BA

#210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#BCBCBCA

