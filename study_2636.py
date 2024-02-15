# # 구해야하는것:
# # 치즈가 모두 녹아 없어지는데 걸리는 시간
# # 모두 녹기 한시간 전에 남아있는 치즈조각이 놓여있는 칸의 개수
# # 비슷한 문제 : boj 2638

# # 치즈 칸(1)의 상하좌우 칸이 외부 공기(0)라면, 치즈를 녹인다.

# from collections import deque
# from sys import stdin
# input = stdin.readline
    
# def bfs():
#     q = deque()
#     check = [[False]*m for _ in range(n)]
#     q.append((0,0))
#     check[0][0] = True
#     while q:
#         x, y = q.popleft()
#         for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
#             nx, ny = x+dx, y+dy
#             if nx<0 or nx>=n or ny<0 or ny>=m: #이거 까먹었었..
#                 continue

#             if not check[nx][ny]: # 중복방문 방지
#                 if a[nx][ny] >= 1:
#                     a[nx][ny] += 1
#                 else:
#                     q.append((nx,ny))
#                     check[nx][ny] = True

# # 예외처리하기
# def melt():
#     global ans2
#     ans2 = 0
#     # melted = False
#     cntcheeze = 0
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] >= 2:
#                 a[i][j] = 0
#                 # melted = True
#                 ans2 += 1
#             elif a[i][j] == 1:
#                 cntcheeze += 1
#                 ans2 += 1
#     return cntcheeze # 남아있는 치즈 갯수 (있으면 true 없으면 false)

# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# ans, ans2 = 0, 0

# while True:
#     bfs()
#     cheeze = melt()
#     ans += 1
#     if cheeze: # 치즈 남아있으면
#         ans2 = cheeze # ans2 업데이트
#     else: # 남은 치즈 갯수가 0개이면
#         if(ans2 == 0):
#             ans -= 1
#         break
    

# print(ans)
# print(ans2)

from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    check = [[False]*m for _ in range(n)]
    q.append((0,0))
    check[0][0] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not check[nx][ny]: #이거 빼먹음
                if a[nx][ny] >= 1:
                    a[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    check[nx][ny] = True


def melt(): 
    global meltedchz 
    cntmelted = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 2: #녹을 치즈가 있으면
                a[i][j] = 0 #치즈 녹이고
                melted = True
                cntmelted += 1 #녹인거 갯수 센다

    if cntmelted: #녹은 치즈가 있을때만
        meltedchz = cntmelted #이번 시간에 녹은 치즈양 새롭게 업데이트
    return cntmelted #이번 시간에 녹은 치즈양 반환

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
time, meltedchz = 0, 0 

while True:
    bfs()
    if melt(): #녹은게 있으면
        time += 1
    else: #녹은게 없다면
        break #반복문 중단

    #1시간전까지 남아있던 치즈갯수 구하기 = 이게 포인트

print(time)
print(meltedchz)