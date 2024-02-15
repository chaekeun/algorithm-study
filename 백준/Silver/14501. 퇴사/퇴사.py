from sys import stdin
input = stdin.readline

n = int(input())
t, p = [0]*(n+1), [0]*(n+1)
ans = 0
for i in range(1, n+1): #1일째부터 시작함
    t[i], p[i] = map(int, input().split())


def solve(day, profit):
    global ans
    if day == n+1:
        ans = max(ans, profit)
        return
    if day > n+1:
        return
    solve(day+t[day], profit+p[day])
    solve(day+1, profit)

solve(1,0)
print(ans)