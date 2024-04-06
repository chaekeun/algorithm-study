from sys import stdin
from itertools import combinations
input = stdin.readline

n = int(input())
straws = [int(input().strip()) for _ in range(n)]
ans = -1

straws.sort(reverse=True)

for i in range(n-2):
    k = straws[i+1]+straws[i+2]

    if k > straws[i]:
        ans = straws[i] + k
        break


print(ans)