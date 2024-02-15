import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y, r):
    # area = 1
    check[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,1),(0,-1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if not check[nx][ny] and a[nx][ny] > r:
                dfs(nx, ny, r)
    # return area 
    # 이렇게하면 아무 지역도 물에 잠기지 않는 경우를 처리하지 못한다.
    
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0


for k in range(max(map(max, a))):
    check = [[False]*n for _ in range(n)] #이거 빼먹었었음
    cnt = 0 #이거 빼먹었었음 k마다 초기화해주는것
    for i in range(n):
        for j in range(n):
            if not check[i][j] and a[i][j] > k: #이거 빼먹었었음
                # 아무 지역도 물에 잠기지 않을수 있기 때문이다.
                # cnt += dfs(i, j, k)
                dfs(i,j,k)
                cnt += 1
    ans = max(ans, cnt)

print(ans)