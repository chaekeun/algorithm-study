# 치즈(1)의 상하좌우 중 적어도 2변 이상이 외부공기와 접촉하면 한시간만에 녹는다.
# 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하시오.

# 근데 내가 어려운것..   내부공기랑 맞닿는 치즈는 녹지 않는다는 조건을 처리하는 것.. -> 외부공기를 q에 넣으면서 주변을 탐색하므로 내부 공기가 q에 들어올 일이 없다.

# 인접한 상하좌우 칸이 공기(0)이라면 아무것도 안하고 그냥 이동한다.
# 인접한 칸이 치즈(1)라면, 치즈를 1만큼 증가시킨다.
# bfs 탐색이 완료되면, 치즈는 1 이상의 값으로 된다. = 기존 치즈(1)값 + 인접한 공기의 갯수
# - if 치즈값 >= 3 then 치즈를 녹여서 공기칸(0)으로 만든다.
# - if 치즈값 ==2 then 치즈를 1로 다시 돌려놓는다.

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
            if not check[nx][ny]: #중복방문 방지(치즈면 여러번 방문하긴 할것)
                if a[nx][ny] >= 1: #치즈면 
                    a[nx][ny] += 1 #인접 외부 공기 갯수 count를 위해 +=1
                else:
                    q.append((nx, ny)) #공기이면 근처 치즈에 영향을 미치기 위해 q.append
                    check[nx][ny] = True 

def melt():
    melted = False
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 3:
                a[i][j] = 0 
                melted = True
            elif a[i][j] == 2:
                a[i][j] = 1
    return melted # 더이상 녹을게 없으면(a[i][j]>=3이면) melted == False 


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0 

while True:
    bfs() # bfs를 통해 치즈값을 인접 외부공기 갯수로 업데이트 해주고
    if melt(): # n*m 한번 돌면 if문 끝나는 것
        ans += 1
    else: # melted==False이면 더이상 녹을 것이 없으므로
        break

print(ans)



