#141
리스트 = [100, 200, 300]
for x in 리스트:
    print(x+10)

#142
리스트 = ["김밥", "라면", "튀김"]
for x in 리스트:
    print("오늘의 메뉴:",x)

#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for x in 리스트:
    print(len(x))

#144
리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    print(x,len(x))

#145
for x in 리스트:
    print(x[0])

#146
리스트 = [1, 2, 3]
for x in 리스트:
    print('3 x',x)

#147
for x in 리스트:
    print('3 x',x,'=',(3*x))

for 변수 in 리스트:
  print("3 x {} = {}".format(변수, 3 * 변수))

#148
리스트 = ["가", "나", "다", "라"]
for x in 리스트[1:]:
    print(x)

#149
for x in 리스트[::2]:
    print(x)

#150
for x in 리스트[::-1]:
    print(x)