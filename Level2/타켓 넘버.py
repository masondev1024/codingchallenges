# 프로그래머스 - 타켓 넘버
# 레벨: 2

def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(idx+1, total + numbers[idx])
        dfs(idx+1, total - numbers[idx])
    dfs(0, 0)
    return answer