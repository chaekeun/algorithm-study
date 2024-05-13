from sys import stdin
input = stdin.readline

n = int(input())
dp = [-1]*10001

dp[1], dp[2] = -1, -1
dp[3] = 1
dp[4] = -1
dp[5] = 1

for i in range(6, n+1):
    if min(dp[i-5], dp[i-3]) > 0:
        dp[i] = min(dp[i-5], dp[i-3])+1
    else:
        if max(dp[i-5], dp[i-3]) > 0:
            dp[i] = max(dp[i-5], dp[i-3])+1
        else:
            dp[i] = -1


print(dp[n])