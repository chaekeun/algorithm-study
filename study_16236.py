# 조건 정리해보기
# 1. 처음 아기 상어의 크기는 2이다.
# 2. 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 3. 자신의 크기보다 작은 물고기만 먹을 수 있다.

# 먹을 물고기를 결정하는 것이 핵심
# 4. 상어에게 가장 가까운 위치에 있는 물고기를 우선순위로 먹어야 한다.
# 5. 여러마리가 가까이에 있다면, 가장 위쪽에 있는 물고기 (ft.행), 그 다음 순서로 가장 왼쪽에 있는 물고기(ft.열)를 우선순위로 먹어야 한다.
# -> 4, 5번때문에 minheap에 (이동거리, 행좌표, 열좌표)를 push하는 것
# 6. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.

#

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# q = []

# def init():
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == 9:
#                 heappush(0, i, j)
#                 a[i][j] = 0
#                 return

# def bfs():
#     body,eat,ans = 2,0,0
#     check = [[False]*n for _ in range(n)]

#     while q:
#         d,x,y = heappop(q)
#         if 0 < a[x][y] < body:
#             eat += 1
#             a[x][y]=0
#             if eat == body:
#                 body+=1
#                 eat=0
#             ans += d
#             d=0
#             while q:
#                 q.pop()
#             check = [[False]*n for _ in range(n)]

#         for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
#             nd, nx, ny = d+1, x+dx, y+dy
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if 0<a[nx][ny]>body or check[nx][ny]:
#                 continue
#             check[nx][ny]=True
#             heappush(q, (nd,nx,ny))
#     print(ans)

# init()
# bfs()


# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# q = []

# def init():
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == 9:
#                 heappush(q, (0, i, j))
#                 a[i][j] = 0
#                 return

# def bfs():
#     body, eat, ans = 2, 0, 0

#     while q:
#         d, x, y = heappop(q)
#         if 0<a[x][y]<body:
#             eat+=1
#             a[x][y]=0
#             if eat==body:
#                 body+=1
#                 eat=0
#             ans+=d
#             d=0
#             while q:
#                 q.pop()
#             check=[[False]*n for _ in range(n)]

#         for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
#             nd,nx,ny = d+1,x+dx,y+dy
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if 0<a[nx][ny]>body or check[nx][ny]:
#                 continue
#             check[nx][ny]=True
#             heappush(q, (nd,nx,ny))
#     print(ans)

# init()
# bfs()

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
q=[]


def init():
    for i in range(n):
        for j in range(n):
            if a[i][j]==9:
                heappush(q, (0, i, j))
                a[i][j]=0
                return

def bfs():
    body, eat, ans=2, 0, 0
    check = [[False]*n for _ in range(n)]

    while q:
        d, x, y = heappop(q)
        if (0<a[x][y]<body):
            eat+=1
            ans+=d
            d=0
            a[x][y]=0
            if (eat==body):
                body+=1
                eat=0
            while q:
                q.pop()
            check=[[False]*n for _ in range(n)]
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
            nd, nx, ny = d+1, x+dx, y+dy
            if (nx<0 or nx>=n or ny<0 or ny>=n):
                continue
            if (0<a[nx][ny]>body or check[nx][ny]):
                continue
            heappush(q, (nd, nx, ny))
            check[nx][ny]=True
    print(ans)

init()
bfs()
