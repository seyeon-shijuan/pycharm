#071
my_variable= ()
print(type(my_variable)) #<class 'tuple'>

#072
movie_rank = ('닥터 스트레인지','스플릿','럭키')
print(movie_rank) #('닥터 스트레인지', '스플릿', '럭키')

#073
mytuple = (1)
print(type(mytuple)) #<class 'int'>
mytuple = (1, )
print(type(mytuple)) #<class 'tuple'>
#튜플 할거면 ,쉼표를 써야 한다.

#074
t = (1, 2, 3)
#t[0] = 'a'
#안되는 이유 > 튜플은 엘리먼트를 바꿀 수 없는 불가변 리스트이기 떄문이다.

#075
t = 1, 2, 3, 4
print(type(t)) #<class 'tuple'>
#튜플은 () 이긴한데, () 없어도 튜플된다.

#076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t) #('A', 'b', 'c')
#튜플 내용을 바꾸고 싶으면 그냥 같은 변수멍에 다시 declare하면 된다.

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest)) #<class 'list'>

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(type(interest)) #<class 'tuple'>

#079
temp = ('apple', 'banana', 'cake')
a, b, c= temp
print(a, b, c) #apple banana cake
#잘라서 a, b, c 하면 따로 들어간다.

temp1 = ('apple', 'banana', 'cake')
one = temp1
two = temp1
three = temp1
print(one, two, three)
#한방에 다들어간다.

#080
print(tuple(range(2, 100, 2)))
#(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)


