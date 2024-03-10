from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
cnt = 0
q = []
    
def solve(cnt):

    if cnt == m:
        print(" ".join(map(str, q)))
        return

    for i in range(n):
        q.append(i+1)
        solve(cnt+1)
        q.pop()
        
solve(cnt)  
