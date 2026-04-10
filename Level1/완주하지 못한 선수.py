from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    
    return list(answer.keys())[0]


# 다른 풀이

def solution(participant, completion): # Dictionary(Hash Table) 직접 사용
    hash_dict={}

    #참여자 이름을 키로 하여 카운트
    for p in participant:
        hash_dict[p] = hash_dict.get(p,0) + 1 # 딕셔너리에서 get(key) 과 [key] 를 조회할 때 차이점은 존재하지 않는 키를 조회할때 발생하는 동작
        # 만약 여기서 get()가 아니라 [key]를 통해 value를 가져오면 participant에 없는 키값을 넣으면 Error가 발생, get()는 None을 출력
        # get() 메서드는 키가 없을 때 반환할 기본값(0)을 설정
    
    #완주자 이름을 키로 하여 해당되는 value에 -1 한 값 저장
    for c in completion:
        hash_dict[c] -= 1

    for key in hash_dict:
        if hash_dict[key] >0:
            return key
