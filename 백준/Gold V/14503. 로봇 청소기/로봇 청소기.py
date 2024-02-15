n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

def solve(x, y, z):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
 
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if i == 3 and a[nx][ny] != 0:
            if a[x-dx[z]][y-dy[z]] == 1:
                break
            else:
                solve(x-dx[z], y-dy[z], z)
                break
        if a[nx][ny] == 0:
            while True:
                z = int((z+(4-1))%4)
                if a[x+dx[z]][y+dy[z]] == 0:
                    solve(x+dx[z], y+dy[z], z)
                    break
            break
  
    return ans
           

solve(r, c, d)
print(ans)