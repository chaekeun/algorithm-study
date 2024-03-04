def solution(s):

    answer = True
    cnt = 0
    for b in s:
        if b == '(':
            cnt += 1
            continue
        cnt -= 1
        if cnt == -1:
            answer = False
            break
    if cnt:
        answer = False
        
    return answer