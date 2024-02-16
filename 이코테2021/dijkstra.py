# import sys
# input = sys.stdin.readline
# inf = int(1e9)

# n, m = map(int, input().split())

# start = int(input())
# #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
# graph = [[] for i in range(n+1)]

# visited = [False]*(n+1)
# distance = [inf] *(n+1)

# for _ in range(m):
#     a,b,c = map(int, input().split()) #a에서 b노드로 가는 비용이 c
#     graph[a].append((b,c)) #a번째 list에 b와 c를 하나의 튜플로 묶어서 append

# #방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = inf
#     index = 0
#     for i in range(1, n+1): #모든 노드를 한번씩 확인 (선형탐색)
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for j in graph[start]: #시작노드에서 당장 도달가능한 노드까지의 거리 갱신
#         distance[j[0]] = j[1] 
    
#     #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n-1):
#         #현재 최단 거리가 가장 짧은 노드를 꺼내서
#         now = get_smallest_node()
#         visited[now] = True #방문처리

#         #현재 노드의 인접 노드들을 확인
#         for j in graph[now]:
#             #시작노드~현재노드~다른노드 의 거리 = 현재노드까지의 최단거리 + 현재노드에서 다른 노드까지의 거리
#             cost = distance[now] + j[1] 
            
#             #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost #최단거리 테이블 갱신

import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
#각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
#최단거리 테이블 초기화
distance = [inf]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미

def dijkstra(start):
    q = []
    #시작노드로 가기 위한 최단거리는 0으로 설정하여 큐에 삽입한다. (최단거리, 노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 - 라이브러리가 알아서 최단거리 짧은 순서대로 pop해주기 때문
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 distance[now]가 최단거리로 업데이트 되었을거니까
        if distance[now] < dist: 
            continue
        #현재 노드의 인접 노드들을 확인하면서
        for i in graph[now]: 
            cost = dist + i[1] # cost = ~now노드~인접노드 를 거치는 거리 = 현재 노드를 거쳐서 다른 노드로 이동하는 거리
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 기존 최단거리보다 짧으면
            if cost < distance[i[0]]:
                distance[i[0]] = cost #최단거리테이블 갱신
                heapq.heappush(q, (cost, i[0])) #값이 갱신될때마다 해당 정보를 우선순위큐에 기록

dijstra(start)