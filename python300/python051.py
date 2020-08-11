#051
movie_rank = ["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

#052
movie_rank.append("배트맨")
print(movie_rank) #['닥터 스트레인지', '스플릿', '럭키', '배트맨']

#053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')
print(movie_rank) #['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

#054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
print(movie_rank) #['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

#055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[3]
print(movie_rank) #['닥터 스트레인지', '슈퍼맨', '스플릿']
del movie_rank[2]
print(movie_rank) #['닥터 스트레인지', '슈퍼맨']

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1+lang2
print(langs) #['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
#list는 그냥 더하면 더해진다.

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums)) #15

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook)) #12

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums)) #3.0



