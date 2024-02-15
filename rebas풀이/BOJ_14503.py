n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a[x][y] = 2
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def solve(x, y, d, ans):

    while True:
        c = False #flag를 사용하는 것이 낯설다
        for k in range(4):
            nd = (d+3)%4 #반시계방향 회전
            nx, ny = x+dx[nd], y+dy[nd] 
            d = nd
            if not a[nx][ny]: #만약 빈공간이면
                a[nx][ny] = 2 
                ans += 1
                x, y = nx, ny
                c = True
                break #더 확인할 필요 없으므로 for문 종료

        if not c: #만약 청소를 했었다면 c = True이므로 if문이 실행되지 않는다
            if a[x-dx[d]][y-dy[d]] == 1: #후진하려는 칸이 벽일 경우
                return ans #함수 종료
            else:
                x, y = x-dx[d], y-dy[d]

print(solve(x, y, d, 1))

def solve(x, y, d, ans):
    c = False
    for k in range(4):
        nd = (d+3)%4
        nx, ny = x+dx[nd], y+dy[nd]
        d = nd
        if not a[nx][ny]: #0 == False
            a[nx][ny] = 2
            ans += 1
            x, y = nx, ny
            c = True #한칸이라도 청소할 수 있다는 flag
            break
    
    if not c: #한칸도 청소할 수 없다면
        if a[x-dx[d]][y-dx[y]] == 1: #종료조건
            return ans 
        else:
            x, y = x-dx[d], y-dy[d]