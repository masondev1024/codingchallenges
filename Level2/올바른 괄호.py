
# 내 풀이 <- 엄밀히 말하면 이건 스택으로 푼게 반쯤 맞음. 왜냐하면 스택에 다 쌓으면서 푼게 아니라 '('만 스택에 쌓고 ')'는 스택에 넣지 않고 trash로 취급했기 때문
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

# 내가 다시 풀었을 떄 풀이 2
def solution(s):
    stack= []
    answer=True
    for i in s:
        if len(stack)==0:
            if i != '(':
                answer=False
                break
            else:
                stack.append(i)
                continue
        if i ==')':
            stack.pop()
        else:
            stack.append(i)
    if len(stack) !=0 :
        answer = False
    
    
    return answer
            



