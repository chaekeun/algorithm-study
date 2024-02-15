n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
v, safe, virus = [], -3, 100

def dfs(x, y):
    res = 1
    c[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not (c[nx][ny] or a[nx][ny]):
            res += dfs(nx, ny) 
    return res 