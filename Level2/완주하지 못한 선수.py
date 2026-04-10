

# collections.Counter 활용

from collections import Counter

def solution(participant, completion):
    # 1. 각 배열의 빈도수를 계산하여 뺍니다.
    answer = Counter(participant) - Counter(completion)
    
    # 2. 남은 요소의 key 값을 반환합니다.
    return list(answer.keys())[0]


# Dictionary  활용

def solution(participant, completion):
    hash_dict = {}
    
    # 참가자 명단 카운팅
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1
        
    # 완주자 명단 제외
    for c in completion:
        hash_dict[c] -= 1
        
    # 남은 한 명 찾기
    for key, value in hash_dict.items():
        if value > 0:
            return key