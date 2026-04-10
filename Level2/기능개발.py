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