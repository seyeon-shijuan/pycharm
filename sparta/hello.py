fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count =0
for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

#list인데 안에 dictionary가 있다.

for person in people:
    if person['age']>20:
        print(person['name'])

#반복문 안에 조건문 사용하기

myemail = 'sparta@naver.com'
print(myemail)
# result=myemail.split('@')[1].split('.')[0]
# print(result) #naver

#바꾸기
result= myemail.replace('naver','gmail')
print(result)
