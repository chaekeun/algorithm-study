from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    q.append((0,0))
    check = [[False]*m for _ in range(n)]
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not check[nx][ny]:
                if a[nx][ny] >= 1:
                    a[nx][ny] += 1
                else:
                    q.append((nx,ny))
                    check[nx][ny] = True

def melt():
    global piece 
    melted, cnt = False, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 2:
                a[i][j] = 0
                melted = True
                cnt += 1 #녹인 치즈 갯수 cnt
    if cnt: #녹인 치즈가 존재하면
        piece = cnt #녹인 갯수를 전역변수에 저장한다
    return melted 

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans, piece = 0, 0

while True:
    bfs()
    if melt(): # 만약 치즈 녹였었으면
        ans += 1
    else: # melted==False이면 더이상 녹일 치즈가 없으므로
        break

print(ans)
print(piece)