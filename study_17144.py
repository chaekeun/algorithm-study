#약간 연구소 문제 느낌

from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
ans = 0

def diffusion(x, y):
    dust = a[x][y] // 5
    cnt = 0
    for dx, dy in (-1,0),(0,1),(1,0),(0,-1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        if a[nx][ny] == -1:
            continue
        a[nx][ny] += dust
        cnt += 1

    a[x][y] -= dust*cnt

def clean1(x): #x는 공청기 좌표
    a[x-1][0] = 0
    for i in range(x-1, 0, -1):
        a[i][0] = a[i-1][0]
    for j in range(0, c-1):
        a[0][j] = a[0][j+1]
    for i in range(0, x):
        a[i][c-1] = a[i+1][c-1]
    for j in range(c-1, 1, -1):
        a[x][j] = a[x][j-1]
    a[x][1] = 0


def clean2(x):
    for j in range(c-1, 1, -1):
        a[x][j] = a[x][j-1]
    for i in range(r-1, x, -1):
        a[i][c-1] = a[i-1][c-1]
    for j in range(0, c-1):
        a[r-1][j] = a[r-1][j+1]
    for i in range(x+1, r-1):
        a[i][0] = a[i+1][0]
    a[x][1] = 0

def solve(dusts):
    for dx, dy in dusts:
        diffusion(dx, dy)
    clean1(cleaners[0])
    clean2(cleaners[1])

for time in range(t):
    dusts=[]
    cleaners=[]

    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                dusts.append((i, j))
            if a[i][j] == -1:
                cleaners.append(i)
          

    solve(dusts)

print()
for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            ans += a[i][j]
        print(a[i][j], end = " ")
    print()

print(ans)