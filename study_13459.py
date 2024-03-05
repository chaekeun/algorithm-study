from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
a = [input().strip() for i in range(n)]
rx, ry, bx, by = 0, 0, 0, 0

def init():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j

def move(방향):
    if rx == bx and ry == by:
        


def solve():
    만약 R이 구멍에 아직 도달하지 못했다면
    계속 move해야한다
    cnt = 0
    
    while q:
        if a[bx][by] == 'O':
            continue
        if a[rx][ry] == 'O':
            return cnt
        if a[rx][ry] != '#' and a[bx][by] != '#':
            move()