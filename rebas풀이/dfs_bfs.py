def dfs(graph, node, visited):
    visited[node] = True
    #탐색노드 출력
    print(node, end="")
    #한 노드로부터 인접한 다른 노드를 재귀적으로 방문 처리
    for i in graph[node]:
        if not (visited[i]):
            dfs(graph, i, visited)

from collections import deque

def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    #큐가 완전히 빌 때까지 반복
    while queue:
        #큐에 삽입된 순서대로 노드 하나 꺼내기
        v. queue.popleft()
        #탐색순서 출력
        print(v, end='')
        #현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
