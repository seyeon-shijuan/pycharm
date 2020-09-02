#251
'''
클래스: frame
객체: 클래스에 의해 만들어진 실체
인스턴스: 클래스에 의해 만들어진 객체
'''

#252
class Human:
    pass

#253
areum = Human()

#254
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

#255
class Human:
    def __init__(self, name, age, sex):
        self.name=name #생성자
        self.age=age
        self.sex=sex

areum= Human("아름",25,"female")
print(areum.name)

#256
print(areum.age)
#생성자는 .으로 접근한다.

#257
class Human:
    def __init__(self, name, age, sex):
        self.name=name #생성자
        self.age=age
        self.sex=sex
    def who(self):
        print("이름:",self.name,"나이:",self.age,"성별:",self.sex)

areum= Human("아름",25,"female")
areum.who()

#258
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자")
areum.who()      # Human.who(areum)

#259
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)

#260
class OMG :
    def print() :
        print("Oh my god")

myStock = OMG()
myStock.print()