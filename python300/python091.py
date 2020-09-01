#091
#Dictionary 만들기
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]
             }
print(inventory)

#092
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][0]) #300

#093
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][1],"개") #20 개

#094
#Dictionary 추가
inventory["월드콘"]=[500,7] #{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}
print(inventory)

#095
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice=list(icecream.keys())
print(ice) #['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']

#096
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice=list(icecream.values())
print(ice) #[1200, 1200, 1800, 1500, 1000]

#097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values())) #6700

#098
#dictionary에 multiple keys values 변수 통째로 추가하기 -> update()
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#099
#zip dict
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
fruits = dict(zip(keys,vals))
print(fruits) #{'apple': 300, 'pear': 250, 'peach': 400}

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)
#{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

