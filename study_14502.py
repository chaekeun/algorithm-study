from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    res = 1
    c[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not (c[nx][ny] or a[nx][ny]):
            res += dfs(nx, ny) #덩어리의 크기를 알려고 할땐 이렇게
    return res


def solve():
    if wall == 3:
        cnt = 0
        for i, j in v:
            cnt += dfs(i, j)
        virus = min(virus, cnt)
        return
    for i in range(x, n):
        k = y if i == x else 0
        for j in range(k, m):
            if a[i][j] == 0:
                a[i][j] = 1
                solve(wall+1, i, j+1)
                a[i][j] = 0


for i in range(n):
    for j in range(m):
        if a[i][j] != 1:
            safe+=1
        if a[i][j] == 2:
            v.append((i,j))
solve(0,0,0)
print(safe-virus)