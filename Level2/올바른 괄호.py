# 프로그래머스 - 올바른괄호
# 레벨: lv2
# 날짜: 2026-03-28

# 내 풀이
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
    

# 다른 사람 풀이
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0

