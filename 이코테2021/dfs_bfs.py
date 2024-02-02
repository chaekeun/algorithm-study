#동빈나 음료수 얼려먹기

# 1. 특정 지점 상하좌우 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 2. 방문한 지점에서 1번 과정 반복 -> 연결된 모든 지점 방문 가능
# 3. 모든 노드에 대하여 1, 2번의 과정 반복 -> 방문하지 않은 지점의 수를 카운트
# 3번이 잘 이해안감

# 내가 시도했던 풀이
from sys import stdin
input = stdin.readline

# n, m = int(input().split())
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(x, y):

    countIce = 1
    visited[x][y] = True

    for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
        nx, ny = x+dx, y+dy
        if (nx<0 or nx>=n or ny<0 or ny>=m):
            return False
        if not (visited[nx][ny] or a[nx][ny]):
            dfs(nx, ny)
            return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result +=1
print(result)

# #동빈나 정답
# def dfs(x, y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#         #해당노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1,y)
#         dfs(x, y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j)==True:
#             result +=1
# print(result)


