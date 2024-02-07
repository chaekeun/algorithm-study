# boj 14502 : 경우의 수들 중 칸의 갯수의 최댓값을 구하는 프로그램
# boj 2468 : 경우의 수들 중 영역(칸의 집합)의 갯수의 최댓값을 구하는 프로그램 
# -> k for문을 돌아야된다는 점 빼고는 동빈나 음료수 얼려먹기랑 다를게 없음

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# check = [[False]*n for _ in range(n)]

# def dfs(x, y, z):
    
#     check[x][y] = True

#     for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
#         nx, ny = x+dx, y+dy
#         if nx<0 or nx>=n or ny<0 or ny>=n:
#             continue
#         if not check[nx][ny] and a[nx][ny] > z:
#             dfs(nx,ny,z)

   

# def solve():
#     global ans
#     ans = 0
#     for k in range(max(max(a))):
#         check = [[False]*n for _ in range(n)]
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 if not check[i][j] and a[i][j]>k:
#                     dfs(i, j, k)
#                     cnt+=1
#         ans = max(ans, cnt)

# solve()
# print(ans)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*n for _ in range(n)]
ans = 0

def dfs(x,y,z):
    check[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if not check[nx][ny] and a[nx][ny] > z:
            dfs(nx, ny, z)



for k in range(max(max(a))):
    check = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j] and a[i][j]>k:
                dfs(i,j,k)
                cnt+=1
    ans = max(ans, cnt)
    
print(ans)    


