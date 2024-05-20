from sys import stdin
from itertools import permutations
input = stdin.readline

n = int(input())
k = int(input())
a = [int(input()) for _ in range(n)]
cnt = 0
ans = []

for p in permutations(a, k):
    temp = ""
    for elem in p: 
        temp += str(elem)
    ans.append(temp)

cnt = len(set(ans))
print(cnt)