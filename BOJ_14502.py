#N*M을 순회하면서 if (0) then (1)
#벽을 두는 함수는 재귀로 구현한다. 
#if (countWall = 3) then DFS(if(0) then (2) and countVirus++)
#answer = max(N*M-countVirus)

#필요한것 : 연구실지도크기, 입력값, dfs를 위한 visited, virus위치들, 안전한 영역의 수, 감염된 영역의 수

#연구실 지도 크기
n, m = map(int, input().split())
#연구실 지도 모양 저장
a = [list(map(int, input().split())) for _ in range(n)] 
#방문 여부를 나타내는 2차원 배열 (dfs)
visited = [[False]*m for _ in range(n)] 
#v는 폭탄의 좌표값 튜플을 요소로 갖는 list
v = []
#안전한 영역의 수 초기화
safe = -3
#감염된 영역의 수 초기화
virus = 100



#기본 dfs에 res와 a[nx][ny]에 대한 조건 추가한 함수
def dfs(x, y):

    #x,y는 시작위치

    countVirus = 1 #?
    
    visited[x][y] = True 

    for dx, dy in (-1,0), (1,0), (0,-1), (0,1): #좌우하상(?)이동을 위한 반복문
        nx, ny = x+dx, y+dy 
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue #범위를 벗어나면 다음 반복으로 넘어간다
        if not(visited[nx][ny] or a[nx][ny]): #인접노드가 방문한적 없거나 입력받은 연구소 지도 좌표가 빈공간 (= 0 = False) 일 경우 if문 실행
            countVirus += dfs(nx, ny) #?
    return countVirus

def solve(wall, x, y):
    global virus, cnt
    if wall == 3:
        cnt = 0
        #이런 초기화방식 익숙해지기
        visited = [[False]*m for _ in range(n)] #방문여부 초기화(backtracking)
        for i, j in v: #폭탄의 좌표값들을 돌면서
            cnt += dfs(i, j) #새롭게 감염된 것까지 포함된 전체 virus들 count
        virus = min(virus, cnt) #가장 작게 감염되었을때를 찾는다
        return 

    for i in range(x, n): #행순회
        #2중루프를 위한 k 초기화
        #솔직히 왜 이렇게 초기화하는지는 잘 모르겠음..
        #그래서 i==x부분 자꾸 틀림
        k = y if i == x else 0 #x행일때만 y열부터 시작하고 나머지는 0부터 순회
        #x행 y열 이전은 부모함수(?)일 것이므로
        for j in range(k, m): #열순회
            if a[i][j] == 0: #빈공간이면
                a[i][j] = 1 #일단 벽을 세워보고
                solve(wall+1, i, j+1) #wall+1값해주고 다음 열로 넘어가서 재귀 (wall == 3일때까지)
                a[i][j] = 0 #재귀 호출 끝나면(backtracking) 벽을 다시 제거하여 이전 상태로 돌아간다.

#연구소의 initial 상태 저장
for i in range(n):
    for j in range(m):
        if a[i][j] != 1: #만약 벽이 아니라면
            safe += 1 #안전영역
        if a[i][j] == 2: #만약 폭탄이 있다면
            v.append((i, j)) #v에 폭탄의 위치를 append

solve(0,0,0)
print(safe-virus)