# # dfs 동작과정

# # 1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
# # 2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상위 노드를 꺼낸다.
# # 3. 2번 과정을 더이상 수행할 수 없을때까지 반복한다.

# def dfs(graph, v, visited):
#     #v는 시작위치
#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i , visited)

# graph = [
#     [],
#     [2,3,7],
#     [1,4,6],
#     [1,5, 7],
#     [2,6],
#     [3,7],
#     [2,4],
#     [1,3]
# ]

# #각 노드가 방문한 정보를 리스트 자료형으로 표현
# visited = [False] * 9

# print("방문순서")
# dfs(graph, 1, visited)

# #2차원 배열인 경우

# def dfs(x, y):

#     visited[x][y] = True
#     print((x, y), end=' ')

#     for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
#         nx, ny = x+dx, y+dy
#         if nx<0 or nx>=n or ny<0 or ny>m:
#             continue
#         if not(visited[nx][ny]):
#             dfs(nx, ny)

# def dfs(x, y):

#     countVirus = 1

#     visited[x][y] = True

#     for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
#         nx, ny = x+dx, y+dy

#         if nx<0 or ny<0 or nx>=n or ny>=m:
#             continue 

#         if not(visited[nx][ny] or a[nx][ny]):
#             countVirus+=dfs(nx, ny)

#     return countVirus


# def solve(wall, x, y):
#     global virus, c

#     if wall == 3:
#         cnt = 0 
#         visited = [[False]*m for _ in range(n)]

#         for i, j in v:
#             cnt+=dfs(i, j)

#         virus = min(virus, cnt)
#         return

#     for i in range(x, n):

#         k=y if i==x else 0


#         for j in range(k,m):
#             if a[i][j]==0:
#                 a[i][j] = 1
#                 solve(wall+1, i, j+1)
#                 a[i][j]=0

# for i in range(n):
#     for j in range(m):
#         if a[i][j]==1:
#             safe += 1

#         if a[i][j]==2:
#             v.append((i,j))

# solve(0,0,0)
# print(safe-virus)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range (n)]
visited=[[False]*m for _ in range(n)]
v, safe, virus=[], -3, 100

def dfs(x, y):

    cntVirus = 1
    visited[x][y]=True

    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        
        if(nx<0 or nx>n or ny<0 or ny>m):
            continue
        if not (visited[nx][ny] or a[nx][ny]):
            cntVirus += dfs(nx,ny)
    return cntVirus

def solved(wall, x, y):

    global cnt, virus

    if (wall == 3):
        cnt = 0
        visited = [[False]*m for _ in range(n)]

        for i, j in v:
            cnt += dfs(i, j)
        virus = min(cnt, virus)
        return

    for ii in range(x, n):
        k=y if ii == x else 0
        for jj in range(k, m):
            if (a[ii][jj]==0):
                a[ii][jj]=1
                solved(wall+1, ii, jj+1)
                a[ii][jj]=0

for i in range(n):
    for j in range(m):
        if (a[ii][jj]!=1): 
            safe+=1
        if (a[ii][jj]==2):
            v.append((ii,jj))

solved(0,0,0)
print(safe-virus)
            


