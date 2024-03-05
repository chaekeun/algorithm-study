from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
check = [False]*n
a = []

def solve(cnt):
    if cnt == m: #정해진 갯수만큼 추가햇으면
        print(" ".join(map(str, a)))
        return 

    for i in range(n):
        if not check[i]:
            check[i]=True
            a.append(i+1)
            solve(cnt+1) 
            a.pop() #이건 왜해주는건지 모르겠음
            check[i] = False #이것도

solve(0)