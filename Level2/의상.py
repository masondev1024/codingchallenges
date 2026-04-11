
# 1차 내 풀이
from collections import Counter
def solution(clothes):
    answer = 0
    for th in clothes:
        th[0], th[1] = th[1],th[0] # 우리가 원하는건 옷종류들인데 이렇게 바꿀필요 없이 따로 리스트를 만들어 종류만 따로 저장하면 됨
    answer=0
    d= Counter(clothes) # Counter 함수는 리스트를 셀수 x , 내부 리스트는 수정가능하기 떄문에 key로 사용 x
    for cate,name in d:
        if answer ==0:
            answer += d[cate]+1
        else:
            answer=answer*(d[cate]+1)
    return answer

# 2차 내 풀이

from collections import Counter
def solution(clothes):
    answer = 0 # 곱셈연산에서 초기값은 0으로 설정하면 안된다
    need=[]
    [need.append(c[1]) for c in clothes]
    d = Counter(need)
    for cate,name in d: # Counter를 돌린 딕셔너리인 d를 for문으로 돌리면 element는 키값만 인자로 받는다
        if answer ==0: 
            answer += d[cate]+1
        else:
            answer=answer*(d[cate]+1)
    answer -=1
    return answer

# 최종 풀이 
def solution(clothes):
    need = []
    for c in clothes:
        need.append(c[1])
    d = Counter(need)
    answer = 1
    for val in d.values():
        answer *= (val+1)
    return answer-1 # 둘다 안입는 경우는 빼야 하기 때문에 -1

# 해시함수로 다시 풀어본 결과
def solution(clothes):
    answer = 1
    hash_set ={}
    for _,v in clothes:
        hash_set[v] = hash_set.get(v,0)+1
    for i in hash_set.values():
        answer *= i+1
    
    return answer-1