from collections import Counter
def solution(nums):
    answer = 0
    total = len(nums)
    pure = Counter(nums)
    sub = len(pure) 
    if total/2 > sub : 
        answer = sub
    else:
        answer = total/2
    return answer

# 다른 사람 풀이 1
def solution(ls):
    return min(len(ls)/2, len(set(ls)))


# 풀이 2

def solution(nums):
    num = {}
    for i in nums:
        if i not in num:
            num[i] = True
    return min(len(nums)/2, len(num))