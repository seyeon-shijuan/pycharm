#완주하지 못한 선수
def solution(participant, completion):
    # dot 접근자로 sort()만 하면 다시 객체에 담지 않아도 된다.
    participant.sort()
    completion.sort()

    #zip 하면 2개의 list를 같이 놓고 자대고 자르는 것처럼 n번째 요소끼리 비교할 수 있다.
    for par, com in zip(participant, completion):
        if par != com:
            return par

    #내용이 전체가 다 똑같으면 completion의 마지막 element에서 for이 끝나기 때문에 participant의 맨 마지막 요소인 [-1]를 return하면 된다.
    return participant[-1]


#전화번호부 목록
def solution(phone_book):
    answer = True
    phone_book.sort()

    #sort한 상태면 12,123,234 등등으로 정렬되기 때문에 앞뒤끼리만 비교하면 된다.
    #마찬가지로 첫 번째 요소를 빼고 2번째부터 끝까지 해서 리스트를 비교한다.
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1): #startswith는 java method랑 동일
            #return False는 그냥 쓰면 된다.
            return False
    return answer

#위장
def solution(clothes):
    #key value dictionary로 만든다.
    answer = {}
    for i in clothes:
        #i[1]면 착장 아이템 종류다.
        #answer dictionary에 추가안되어있으면 1로 만들어서 추가하고, 있으면 숫자를 1을 올린다.
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    #경우의수 계산을 위해서 cnt 객체 생성
    cnt = 1
    # answer의 value 개수만큼 for문을 돌린다.
    for i in answer.values():
        cnt *= (i + 1)
    return cnt - 1