#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:]) #[100, 130, 140, 150, 160, 170]

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) #[1, 3, 5, 7, 9]

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1:len(nums):2]) #[2, 4, 6, 8, 10]
#len(nums)안쓰면 자동으로 끝까지인것으로 간주된다. : 에 의미가 있는 것이 아님

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1]) #[5, 4, 3, 2, 1]

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2]) #삼성전자 Naver

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest)) #삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
#.join은 "" String의 method가 아니라 interest라는 list를 " "로 연결해서 문자열로 리턴하라는
#리스트의 메서드이다. > 자바는 무조건 앞에 내용, 뒤에 메서드이지만
#파이썬은 이 경우처럼 아닌 경우도 있음.

#067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest)) #삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

#068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#069
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest) #['삼성전자', 'LG전자', 'Naver']

#070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) #[1, 2, 3, 4, 5, 9, 10]

