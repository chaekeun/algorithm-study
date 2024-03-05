from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

# 이걸 어케 백트래킹이랑 같이 쓰지..?

for i in range(1, n+1):
    ans = []
    ans.append(i)
    for j in range(1, n+1):
        if i == j :
            continue
        ans.append(j)
        print(ans[0], ans[1], sep=' ')