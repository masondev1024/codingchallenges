# 프로그래머스 - 테이블 해시 함수
# 레벨: 2



def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        row =data[i-1]
        S_i = sum(x%i for x in row)
        answer ^=S_i
    
    return answer