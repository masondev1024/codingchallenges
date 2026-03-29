# 프로그래머스 - 기능개발
# 레벨: 2
# 날짜: 2026-03-29

import math

def solution(progresses, speeds):
    answer =[]
    finish = [math.ceil((100-progresses)/speeds) for progresses, speeds in zip(progresses,speeds)]
    stack=[]
    
    for day in finish:
        if not stack or day <= stack[0]:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack=[day]
    answer.append(len(stack))   
    
    return answer