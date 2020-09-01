#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i,price_list[i])

for i, data in enumerate(price_list):
    print(i, data)

#173
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

#174
for i in range(len(price_list)):
    print(100+i*10,price_list[i])

#175
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[i],my_list[i+1])

#176
my_list = ["가", "나", "다", "라", "마"]
for i in range( len(my_list) - 2 ):
    print(my_list[i], my_list[i+1], my_list[i+2])

print("-----------")
#177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1,0,-1):
    print(my_list[i],my_list[i-1])

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])

for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))
#to the absolute value 마이너스없애줌

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1,len(my_list)-1):
    print(abs(my_list[i-1]+my_list[i]+my_list[i+1])/3)

#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility=[]
for i in range(len(low_prices)):
    volatility.append(abs(high_prices[i]-low_prices[i]))
print(volatility)
