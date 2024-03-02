def solution(progresses, speeds):
    answer = []
    q=[]
    for p, s in zip(progresses, speeds):
        if len(q) == 0 or -((p-100)//s) > q[-1][0]:
            q.append([-((p-100)//s), 1])
        else:
            q[-1][1] += 1
    
    answer = [elem[1] for elem in q]
    return answer
