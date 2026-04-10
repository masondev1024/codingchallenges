
# 다른 사람 풀이
from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    while queue:
        current = queue.popleft() 
        if any(current[0] < q[0] for q in queue): # 스택을 쌓을때 뒤에 붙이는건 append로 할 수 있는데 앞에 붙이고 싶을 때 
            queue.append(current)
        else: 
            answer += 1
            if current[1] == location:
                return answer
            
# 내가 풀이한 것
from collections import deque

def solution(priorities, location):
    q = deque([(idx,pr) for idx, pr in enumerate(priorities)])
    order = 0
    while q:
        current = q.popleft()
        if any(current[1] < pr for _ ,pr in q):
            q.append(current)
        else:
            order+=1
            if current[0] == location:
                return order
        
            
# 내 풀이 
# from collections import deque

# def solution(priorities, location):
#     answer=[]
#     q= deque(priorities)
#     for idx, pr in enumerate(q):
#         if len(answer) ==0 :
#             q.popleft()
#             answer.append((idx,pr))
#             continue         
#         if answer[0][1] >= pr:
#             q.popleft()
#             answer.append((idx,pr))
#         else:
#             q.popleft()
#             answer.insert((idx,pr))
#     for  idx , e in answer:
#         if idx == location:
#             return e
            