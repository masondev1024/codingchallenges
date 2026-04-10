def solution(s):
    sign = 1 
    
    if s[0] == '-':
        s =s[1:]
        sign=-1
    elif s[0] =='+':
        s = s[1:]
        
    result = 0
    for ch in s:
        result = result * 10 + (ord(ch) - ord('0'))
    
    return sign * result
    