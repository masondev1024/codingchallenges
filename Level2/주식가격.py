# 프로그래머스 - 주식가격
# 레벨: 2
# 날짜: 2026-03-28

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] 

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx  
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer