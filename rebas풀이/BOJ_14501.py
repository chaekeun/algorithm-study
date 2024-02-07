# 수익계산 종료 조건 : day == N+1
# 재귀함수 종료 조건 : day > N+1
# day번재 일에 상담을 하는 경우 : solve(day+t[day], profit+p[day])
# day번째 일에 상담을 하지 않는 경우 : solve(day+1, profit)

from sys import stdin
input = stdin.readline

ans = 0

n = int(input()) #퇴사 전 남은 일수
t, p = [0]*(n+1), [0]*(n+1) #t, p 배열 초기화
for i in range(1, n+1): #각 줄별로 할당하는 방식 기억하기
    t[i], p[i] = map(int, input().split()) #t[i], p[i] 입력값 할당


def solve(day, profit):
    global ans
    if day == n+1: 
        if ans < profit: #ans와 profit이 의미하는 바?
            ans = profit
        return
        
    if day > n+1:
        return
    solve(day+t[day], profit+p[day])
    solve(day+1, profit)

solve(1,0)
print(ans)