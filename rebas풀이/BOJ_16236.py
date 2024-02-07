from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] #입력값은 이런식으로 저장하는거 익숙해지기
q = []

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9: #상어가 있는 곳을 찾아서
                heappush(q, (0,i,j))
                # (이동거리, 행좌표, 열좌표)의 튜플을 요소에 추가
                a[i][j] = 0 #이거 왜해주는지 잘 모르겠긴함
                return

def bfs():
    body,eat,ans = 2,0,0
    check = [[False]*n for _ in range(n)]
    while q:
        d,x,y = heappop(q)
        if 0 < a[x][y] < body: #상어보다 작은 물고기가 있는 경우
            eat += 1
            a[x][y]=0
            if eat == body:
                body += 1
                eat = 0 # 먹은 물고기수 초기화해줘야함
            ans += d # 먹은 순간까지 이동한 거리 누적
            d = 0 # 초기화
            while q:
                q.pop() #큐에 들어있는 좌표를 비우는 이유를 잘 모르겠었는데
                #원래 있던 위치에서 가능한 경로를 모두 탐색하며 가장 가까운 물고기(ft. minHeap)를 먹은 셈이므로 그 이후 경로는 버린다
                #사실 그게 그냥 bfs임..
            check = [[False]*n for _ in range(n)] #다음 물고리를 먹기 위해 움직일 때 이미 갔던 곳을 다시 방문할 수 있도록 방문 체크 배열 모두 초기화
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1): #꼭 문제에서 정해진 우선순위 반영하기!!
            nd, nx, ny = d+1, x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if 0<a[nx][ny] > body or check[nx][ny]: #물고기가 존재하는데 물고기 >상어 or 이미 방문한 노드일때는 지나갈수 있는 곳이 아니므로 q에 추가 X

                continue
            check[nx][ny]=True 
            heappush(q, (nd,nx,ny)) #이동한 거리, 새로 이동한 위치 q에 push
    print(ans)

init()
bfs()
