#N*M을 순회하면서 if (0) then (1)
#벽을 두는 함수는 재귀로 구현한다. 
#if (countWall = 3) then DFS(if(0) then (2) and countVirus++)
#answer = max(N*M-countVirus)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)] #연구소 지도 모양을 1차원 array에 저장하는듯
c = [[False]*m for _ in range(n)] #방문 여부를 나타내는 2차원 배열
v, safe, virus = [], -3, 100 #v는 폭탄의 좌표값 튜플을 요소로 갖는 list

def dfs(x, y):
    res = 1 #?
    c[x][y] = True 
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1): #상하좌우 이동을 위한 반복문
        nx, ny = x+dx, y+dy 
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue #범위를 벗어나면 다음 반복으로 넘어간다
        if not(c[nx][ny] or a[nx][ny]): #빈공간 = 0 = False 일 경우 if문 실행
            res += dfs(nx, ny)
    return res 

def solve(wall, x, y):
    global virus, c
    if wall == 3:
        cnt = 0
        c = [[False]*m for _ in range(n)]
        for i, j in v:
            cnt += dfs(i, j)
        virus = min(virus, cnt)
        return 

    for i in range(x, n): #행순회
        #2중루프를 위한 k 초기화
        k = y if i == x else 0
        for j in range(k, m): #열순회
            if a[i][j] == 0: #빈공간이면
                a[i][j] = 1 #일단 벽을 세워보고
                solve(wall+1, i, j+1) #wall+1값해주고 다음 열로 넘어가서 재귀
                a[i][j] = 0 #재귀 호출 끝나면(backtracking) 벽을 다시 제거하여 이전 상태로 돌아간다.

for i in range(n):
    for j in range(m):
        if a[i][j] != 1: #만약 벽이 아니라면
            safe += 1 #안전영역일수도 있음
        if a[i][j] == 2: #만약 폭탄이 있다면
            v.append((i, j)) #v에 폭탄의 위치를 append

solve(0,0,0)
print(safe-virus)