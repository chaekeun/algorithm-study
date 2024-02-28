def solution(citations):
    answer = 0
    for i in range(max(citations)+1):
        cnt = 0
        for citation in citations:
            if citation >= i:
                cnt += 1
        if cnt>=i:
            answer = max(answer, i)
            
    return answer