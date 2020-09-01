#081
#왼쪽부터 8개만 bind 하기
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)

#082
#오른쪽부터 8개만 bind 하기
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*valid_score = scores
print(valid_score)

#083
#가운데 8개만 bind 하기
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*valid_score,_ = scores
print(valid_score)

#084
#temp 이름의 비어있는 딕셔너리 만들기
temp ={}

#085
ice={"메로나":1000,"폴라포":1200,"빵빠레":1800}
print(ice)

#086
#Dictionary에 element 추가하기
ice["죠스바"]=1200
ice["월드콘"]=1500
print(ice) #{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

#087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:",ice['메로나']) #메로나 가격: 1000

#088
#dictionary 값 수정
ice['메로나']=1300
print(ice['메로나']) #1300

#089
#dictionary 값 삭제
del ice['메로나']
print(ice['메로나'])

#090
'''
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'가 오류인 이유
없는 element를 call 했으니까. -> dictionary에 없는 키를 이용해서 인덱싱했기 때문
'''