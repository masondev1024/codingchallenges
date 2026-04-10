
from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            j,_ = stack.pop()
            answer[j]=i-j
        stack.append((i,prices[i]))
    for k,_ in stack:
        answer[k] = len(prices)-k-1
    return answer