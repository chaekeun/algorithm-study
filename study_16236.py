from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
size = 2

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9:
                heappush(q, (0,i,j))
                a[i][j] = 0
                return
                
def bfs():
    while q:
        d, x, y = heappop(q)
        if 0<a[x][y]<body:
            eat += 1
            a[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ans += d
            d=0
            while q:
                q.pop()
        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d+1, x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if 0<a[nx][ny]>body:
                continue
            heappush(q, (nd, nx, ny))

    print(ans)        

