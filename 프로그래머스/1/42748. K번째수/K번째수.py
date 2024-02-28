def solution(array, commands):
    answer = []
    for command in commands:
        cut = []
        for idx in range(command[0]-1, command[1]):
            cut.append(array[idx])
        cut.sort()
        answer.append(cut[command[2]-1])
        
    return answer