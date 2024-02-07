
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
            if nx<0 or nx>=n or ny<0 or ny>=m: #이거 까먹었었..
                continue

            if not check[nx][ny]: # 중복방문 방지
                if a[nx][ny] >= 1:
                    a[nx][ny] += 1
                else:
                    q.append((nx,ny))
                    check[nx][ny] = True

def melt():
    global ans2
    ans2 = 0
    # melted = False
    cntcheeze = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 2:
                a[i][j] = 0
                # melted = True
                ans2 += 1
            elif a[i][j] == 1:
                cntcheeze += 1
                ans2 += 1
    return cntcheeze # 남아있는 치즈 갯수 (있으면 true 없으면 false)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans, ans2 = 0, 0

while True:
    bfs()
    cheeze = melt()
    ans += 1
    if cheeze: # 치즈 남아있으면
        ans2 = cheeze # ans2 업데이트
    else: # 남은 치즈 갯수가 0개이면
        if(ans2 == 0):
            ans -= 1
        break
    

print(ans)
print(ans2)