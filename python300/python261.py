#261
class Stock:
    pass

#262
class Stock:
    def __init__(self,stock,num):
        self.stock=stock
        self.num=num
삼성 = Stock("삼성전자", "005930")
print(삼성.stock)

#263
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name=name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

#264
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code

a = Stock(None, None)
a.set_code("005930")
print(a.code)

#265
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name())
print(삼성.get_code())


#266
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#267
삼성전자=Stock("삼성전자","005930",15.19,1.33,2.83)

#268
#set_per, set_pbr, set_dividend
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self,per):
        self.per=per
    def set_pbr(self,pbr):
        self.pbr=pbr
    def set_dividend(self, devidend):
        self.배당수익률=devidend

#269
삼성전자=Stock("삼성전자","005930",15.19,1.33,2.83)
삼성전자.set_per(12.75)

#270
삼성전자=Stock("삼성전자","005930",15.19,1.33,2.83)
현대차=Stock("현대차","005380",8.70,0.35,4.27)
LG전자=Stock("LG전자","066570",317.34,0.69,1.37)
stocklist = []
stocklist.append(삼성전자)
stocklist.append(현대차)
stocklist.append(LG전자)
for i in stocklist:
    print(i.code,i.name)

