#101
#파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
#bool (boolean 아님)

#102
print(3 == 5) #False (not false)

#103
print(3 < 5) #True

#104
x = 4
print(1 < x < 5) #True and python은 < 이거 2개해도 된다.

#105
print ((3 == 3) and (4 != 3)) #True

#106
print(3 >= 4) #False >=는 됨 =>이렇게는 쓰면안돼고

#107
if 4 < 3:
    print("Hello World")
    #nothing happens

#108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
    #Hi, there > because the result of the if clause is False so the else command was carried out

#109
if True :
    print ("1",end="")
    print ("2",end="")
else :
    print("3")
print("4")
#124

#110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3",end="")
else :
    print("4")
print("5")
#35
