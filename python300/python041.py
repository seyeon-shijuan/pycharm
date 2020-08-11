#041
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker) #BTC_KRW

#042
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker) #btc_krw

#043
mystr = 'hello'
mystr = mystr.capitalize()
print(mystr) #Hello

#044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) #True

#045
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls"))) #True
#2개 or 조건인경우에는 ()안에 "", "" 로 하면 된다.

#046
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020')) #True

#047
a = "hello world"
alist = a.split(" ")
print(alist) #['hello', 'world']

#048
ticker = "btc_krw"
print(ticker.split("_")) #['btc', 'krw']

#049
date = "2020-05-01"
datelist = date.split("-")
print(datelist)
print(datelist[0],"년",datelist[1],"월",datelist[2],"일")

#050
data = "039490     "
print(data.rstrip()) #039490



