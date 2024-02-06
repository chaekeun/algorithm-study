# 구해야하는것:
# 치즈가 모두 녹아 없어지는데 걸리는 시간
# 모두 녹기 한시간 전에 남아있는 치즈조각이 놓여있는 칸의 개수
# 비슷한 문제 : boj 2638

# 치즈 칸(1)의 상하좌우 칸이 외부 공기(0)라면, 치즈를 녹인다.

from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    check = [[False]*m for _ in range(n)]
    q.append((0,0))
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
            nx, ny = x+dx, y+dy
            if not check[nx][ny]: # 중복방문 방지
                if a[nx][ny] >= 1:
                    a[nx][ny] += 1
                else:
                    q.append((nx,ny))
                    check[nx][ny] = True

def melt():
    # melted = False
    cntcheeze = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 2:
                a[i][j] = 0
                # melted = True
            elif a[i][j] == 1:
                cntcheeze += 1
    return cntcheeze # 남아있는 치즈 갯수 (있으면 true 없으면 false)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0 

while True:
    
    bfs()
    cheeze = melt()
    ans += 1
    if cheeze: # 치즈 남아있으면
        ans2 = cheeze # ans2 업데이트
    else: # 남은 치즈 갯수가 0개이면
        break

print(ans)
print(ans2)



