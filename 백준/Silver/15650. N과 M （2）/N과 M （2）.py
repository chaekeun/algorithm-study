from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
check = [False]*n
a = []
cnt = 0

def solve(_cnt, k):
    if _cnt == m:
        print(" ".join(map(str, a)))
        return

    for i in range(k, n):
        if not check[i]:
            a.append(i+1)
            check[i] = True
            solve(_cnt+1, i)
            a.pop()
            check[i] = False


solve(0,0)