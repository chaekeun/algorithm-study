from sys import stdin
input = stdin.readline

n = int(input())
t, p = [0]*(n+1), [0]*(n+1)
dp = [0]*(n+1)

for k in range(1, n+1):
    t[k], p[k] = map(int, input().split())

        # 끝까지 밀고나가보는 힘을 길러보장 ㅠ

# for i in range(1, n+1):
#     if i+t[i]==n+1:
#         dp[i] = p[i]
#         continue
#     if i+t[i] > n+1:
#         continue
#     else:
#         dp[i] = p[i]
#         k = i+t[i]
#         while True:
#             if k+t[k] == n+1:
#                 dp[i] += p[k]
#                 break
#             if k+t[k] > n+1:
#                 break
#             dp[i] += p[k]
#             k = k+t[k]

# print(max(dp))

# i 날짜까지 일했을 때 얻을 수 있는 최대 수익
dp = [0 for _ in range(n+1)]

# bottom up 방식 : 작은 부분문제부터 반복문을 통해 해결해서 큰 문제를 해결한다
# for i in range(1, n+1):
#     for j in range(i+t[i], n+1):
#         if dp[j] < dp[i] + p[i]: # 만약 i날짜에 상담을 하는 경우가 더 이득이라면
#             dp[j] = dp[i] + p[i] # dp테이블 갱신

# print(dp[-1])

# top down 방식 : 작은 문제를 재귀적으로 호출해서 큰 문제를 해결한다
for i in range(n-1, -1, -1):
    # i날짜에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + t[i] > n:
        dp[i] = dp[i+1] #근데 왜 이렇게하는거임?
    else:
        #i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택하여 값을 업데이트한다.
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])