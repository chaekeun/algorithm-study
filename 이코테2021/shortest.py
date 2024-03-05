from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

# inf = int(1e9)
# n, m, c = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance = [inf for _ in range(n+1)]
# q = []

# for i in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y,z))
    

# def dijkstra(start):
#     q = []
#     heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         dist, now = heapppop(q)
#         # 내가 자꾸 헷갈리는 것 : distance[now] vs graph[now]
#         if distance[now] < dist: #이미 최단거리
#             continue
#         for i in graph[now]: 
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heappush(q, (cost, i[0]))

# dijkstra(c)

# cnt = 0
# max_distance = 0

# for d in distance:
#     if d != inf:
#         cnt += 1
#         max_distance = max(max_distance, d)
    
# print(cnt-1, max_distance)

inf = int(1e9)
n, m = map(int, input().split())
graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j], graph[j][i] = 1, 1

print(graph)

x, k = map(int, input().split())

# for i in range(n+1):
#     if graph[1][k] > graph[1][i]+graph[i][k]:
#         graph[1][k] = graph[1][i]+graph[i][k]
#     if graph[k][x] > graph[k][i]+graph[i][x]:
#         graph[k][x] = graph[k][i]+graph[i][x]
# # 이러면 안대는거였음. 그럼 하나의 노드만 거치는 경로로밖에 업데이트 못하므로

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph[1][k]+graph[k][x])

