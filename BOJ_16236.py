from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] #결과 확인해보기
q = []

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9: 
                heappush(q, (0,i,j))
                # (distance, i, j)의 튜플을 요소에 추가
                a[i][j]=0
                return

def bfs():
    body,eat,ans = 2,0,0
    check = [[False]*n for _ in range(n)]
    while q:
        d,x,y = heappop(q)
        if 0 < a[x][y] < body:
            eat += 1
            a[x][y]=0
            if eat == body:
                body += 1
                eat = 0
            ans += d # 이동한 거리 누적
            d = 0 # 초기화
            while q:
                q.pop() #큐에 들어있는 좌표를 비우는 이유를 잘 모르겠다..
            check = [[False]*n for _ in range(n)] #다음 물고리를 먹기 위해 움직일 때 이미 갔던 곳을 다시 방문할 수도 있으므로 방문 체크 배열 모두 초기화
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
            nd, nx, ny = d+1, x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if 0<a[nx][ny] > body or check[nx][ny]: #????
                continue
            check[nx][ny]=True
            heappush(q, (nd,nx,ny))
    print(ans)

init()
bfs()
