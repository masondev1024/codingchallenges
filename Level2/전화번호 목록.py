# 정렬 함수 사용해서 풀이
def solution(phone_book):
    answer = True
    sorted_b =phone_book.sort() # 정렬 함수 무조건 prefix(접두어)끼리 붙는다
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): # 시작문자같은지확인 
            return False
    return answer

# 해시함수 사용하여 풀이
def solution(phone_book):
    answer = True
    hash_set=set(phone_book) 
    # 굳이 리스트를 세트로 바꿔주는 이유는 시간복잡도 측면에서 리스트는 첨부터 전부 찾지만 O(n)
    # 해쉬테이블은 키값인 prefix 바로 찾아감 O(1)
    for num in phone_book:
        for i in range(1,len(num)): # len(num)개의 문자열까지 체크 안하는 이유는 자기 자신은 빼야 하기 때문
            prefix = num[:i]
            if prefix in hash_set:
                return False
    return answer