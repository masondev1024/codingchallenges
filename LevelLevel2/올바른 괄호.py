# 프로그래머스 - 올바른 괄호
# 레벨: Level2
# 날짜: 2026-03-29

def solution(s):
    answer = True
    stack =[]  
    trash = 0
    for e in s:
        if e =='(':
            stack.append(e)
        elif len(stack) >0 and e ==')':
            stack.pop()
        else:
            trash +=1
    if len(stack) ==0 and trash ==0 :
        return answer
    else:
        answer = False
        return answer
            

