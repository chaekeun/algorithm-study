import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())

start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]

visited = [False]*(n+1)
distance = [inf] *(n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) #a에서 b노드로 가는 비용이 c
    graph[a].append((b,c)) #a번째 list에 b와 c를 하나의 튜플로 묶어서 append

#방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = inf
    index = 0
    for i in range(1, n+1): #모든 노드를 한번씩 확인 (선형탐색)
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]: #시작노드에서 당장 도달가능한 노드까지의 거리 갱신
        distance[j[0]] = j[1] 
    
    #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서
        now = get_smallest_node()
        visited[now] = True #방문처리

        #현재 노드의 인접 노드들을 확인
        for j in graph[now]:
            #시작노드~현재노드~다른노드 의 거리 = 현재노드까지의 최단거리 + 현재노드에서 다른 노드까지의 거리
            cost = distance[now] + j[1] 
            
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost #최단거리 테이블 갱신

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("infinity")
    else:
        print(distance[i])