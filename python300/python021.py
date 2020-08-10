#021
#1,3 추출
letters = 'python'
print(letters[0],letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:]) #2210

#023
#시작인덱스:끝인덱스:오프셋
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1]) #NOHTYP

#025
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-"," ")
print(phone_number) #010 1111 2222

#026
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-","")
print(phone_number) #01011112222

#027
url = "http://sharebook.kr"
url = url.split(".")
print(url[1])

#028
#lang = 'python'
#lang[0] = 'P'
#print(lang)
#문자열이 배열처럼 되어있다고 수정할 수 있는 건 아님
#불러오기만 할 수 있다.

#029
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)

#030
string = 'abcd'
string.replace('b', 'B')
print(string)
#string.replace('b','B')만 하면 그냥 새로운 객체를 만들어서 아무데도 안 담는 것임
#아래에서 string을 불러봤자 방금 위에서 수행한거는 자바랑 똑같이 그냥 NEW 객체라서 연관이 없음

