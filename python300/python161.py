#161
for i in range(10):
    print(i,end="")

#162
for i in range(2002,2051,4):
    print(i,end="")
print("-----")
#163
for i in range(3,31,3):
    print(i)

#164
for i in range(100):
    print(99-i,end="")

#165
for i in range(10):
    print(i / 10)

#166
for i in range(1,10):
    print("3 x {} = {}".format(i,3*i))

#167
for i in range(1,10,2):
    print("3 x {} = {}".format(i,3*i))

#168
summ=0
for i in range(1,11):
    summ+=i
print(summ)

#169
oddsum=0
for i in range(1,11,2):
    oddsum+=i
print(oddsum)

#170
oddmul=1
for i in range(1,11,2):
    oddmul*=i
print(oddmul)