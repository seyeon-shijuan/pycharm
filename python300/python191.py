#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
] #이거는 list야, 수수료 0.014 %를 포함한 가격
for x in data:
    for y in x:
        print(y*1.00014) #4%가 0.04니까 1에다 수수료에서 소수점 뒤로 2개 민 값을 더하면 된다.

#192
for x in data:
    for y in x:
        print(y*1.00014)
    print("-"*4)

#193
result=[]
for x in data:
    for y in x:
        result.append(y*1.00014)
print(result)
#[2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772, 15452.163, 15052.107, 15552.177, 14902.086000000001]

#194
result=[]
for x in data:
    sub=[]
    for y in x:
        sub.append(y*1.00014)
    result.append(sub)
print(result)
#[[2000.28, 3050.427, 2050.2870000000003, 1980.2772], [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772], [15452.163, 15052.107, 15552.177, 14902.086000000001]]

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc[1:]:
    print(x[3])
'''
100
190
310
'''

#196
for x in ohlc[1:]:
    if x[3]>150:
        print(x[3])
print()

#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc[1:]:
    if x[3]>=x[0]:
        print(x[3])

#198
volatility=[]
for x in ohlc[1:]:
    volatility.append(x[1]-x[2])
print(volatility)

#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc[1:]:
    if x[3]>x[0]:
        print(x[1]-x[2])

#200
#시가에 매수해서 종가에 매도 했을 경우 총 수익금
amount=0
for x in ohlc[1:]:
    amount+= x[3]-x[0]
print(amount)
