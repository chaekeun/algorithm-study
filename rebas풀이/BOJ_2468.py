#물에 잠기지 않는 안전 영역의 최대 개수를 구하는 문제
#dfs로 영역을 완전 탐색하면서 영역의 개수를 센다

# 입력으로 주어지는 값에서 가장 큰 값을 M이라 둔다
# 0부터 M-1까지 제한높이 k를 올리면서 dfs를 돌린다
# dfs로 탐색할때, 잠기지 않는 영역으로 이동한다. 이동하면서 방문체크를 한다
# 아직 방문하지 않은 곳이면서 높이가 k보다 높다면, 다시 dfs로 탐색한다 
# -> 인접한 부분까지 count하기 위해
# if n*n사이즈 맵을 모두 visited then 제한 높이를 1 올리고 다시 dfs 반복


#     #boj 14502 연구소 문제에서도 전역변수를 이용하여 가장 작게 감염되었을때를 찾았는데 dfs에서 그런 구현이 자주 등장하는 듯

import sys
sys.setrecursionlimit(1000000)

def dfs(x, y, z):
    check[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>= n:
            continue
        if not check[nx][ny] and a[nx][ny]>z:
            dfs(nx, ny, z)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for k in range(max(map(max, a))):
    check = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j] and a[i][j] >k:
                dfs(i, j, k)
                cnt+=1 #덩어리의 갯수
    ans = max(ans, cnt)
    
print(ans)