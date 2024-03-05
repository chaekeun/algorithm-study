from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
rx, ry, bx, by = 0,0,0,0
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def init():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                rx, ry = i, j
            if a[i][j] == 'B':
                bx, by = i, j

def move()