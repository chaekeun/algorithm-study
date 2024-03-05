# #동빈나 음료수 얼려먹기

# # 내가 시도했던 풀이
# from sys import stdin
# input = stdin.readline

# n, m = int(input().split())
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False]*m for _ in range(n)]

# def dfs(x, y):

#     countIce = 1
#     visited[x][y] = True

#     for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
#         nx, ny = x+dx, y+dy
#         if (nx<0 or nx>=n or ny<0 or ny>=m):
#             return False
#         if not (visited[nx][ny] or a[nx][ny]):
#             dfs(nx, ny)
#             return True
#     return False


# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j)==True:
#             result +=1
# print(result)

# #동빈나 정답
# # def dfs(x, y):
# #     if x<=-1 or x>=n or y<=-1 or y>=m:
# #         return False
# #         #해당노드를 아직 방문하지 않았다면
# #     if graph[x][y] == 0:
# #         graph[x][y] = 1
# #         #연결된 지점을 방문처리 하기 위한 목적
# #         #solve부분에서 return값을 사용하지 않기 때문에 result에는 반영되지 X
# #         dfs(x-1,y)
# #         dfs(x, y-1)
# #         dfs(x+1,y)
# #         dfs(x,y+1)
# #         return True
# #     return False

# # result = 0
# # for i in range(n):
# #     for j in range(m):
# #         #현재 위치에서 dfs 수행 
# #         #해당 노드와 연결된 모든 노드들도 방문처리 할 수 있게 된다.
# #         #현재 노드에서만 result값이 증가(인접노드들에 대해선 result값 처리 X)
# #         if dfs(i, j)==True:
# #             result +=1
# # print(result)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
    
#     while queue:
#         v = queue.popleft()

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))