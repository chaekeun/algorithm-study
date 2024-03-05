from sys import stdin
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
# i 날짜까지 일했을 때 얻을 수 있는 최대 수익
dp = [0 for _ in range(n+1)]

# # bottom up 방식 : 작은 부분문제부터 반복문을 통해 해결해서 큰 문제를 해결한다
# for i in range(n):
#     for j in range(i+schedule[i][0], n+1):
#         if dp[j] < dp[i]+schedule[i][1]: #i번째 날의 상담을 했을때가 profit이 더크다면 갱신
#             dp[j] = dp[i]+schedule[i][1]

# print(dp[-1])

# top down 방식 : 작은 문제를 재귀적으로 호출해서 큰 문제를 해결한다
