def solution(priorities, location):

    q = [[_idx, _prior] for _idx, _prior in enumerate(priorities)]
    result = []
    answer = 0
    
    while q:
        flag = True
        idx, prior = q.pop(0)
        for elem in q:
            if elem[1] > prior:
                q.append([idx, prior])
                flag = False
                break
        if flag:
            result.append(idx)

    for i in range(len(result)):
        if location == result[i]:
            answer = i+1
    return answer