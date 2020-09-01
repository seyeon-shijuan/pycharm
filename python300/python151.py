#151
리스트 = [3, -20, -3, 44]
for x in 리스트:
    if x <0:
        print(x)

#152
리스트 = [3, 100, 23, 44]
for x in 리스트:
    if x % 3 ==0:
        print(x)

#153
리스트 = [13, 21, 12, 14, 30, 18]
#20 보다 작은 3의 배수
for x in 리스트:
    if x <20 and x%3==0:
        print(x)

#154
리스트 = ["I", "study", "python", "language", "!"]
for x in 리스트:
    if len(x)>2:
        print(x)


#155
리스트 = ["A", "b", "c", "D"]
for x in 리스트:
    if not(x.islower()):
        print(x) # isupper() 있음..

#156
리스트 = ["A", "b", "c", "D"]
for x in 리스트:
    if x.islower():
        print(x)

#157
리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    print(x[0].upper()+x[1:])

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for x in 리스트:
    print(x.split(".")[0])

#159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in 리스트:
    if x.split(".")[1]=='h':
        print(x)

#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in 리스트:
    if x.split(".")[1]=='h' or x.split(".")[1]=='c':
        print(x)