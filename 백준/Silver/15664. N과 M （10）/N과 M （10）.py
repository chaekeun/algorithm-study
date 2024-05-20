# 입력 받기
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 초기화
check = [False] * n
v = []
s = set()


def solve(cnt, idx):
    if cnt == m:
        s.add(tuple(v))
        return
    
    for i in range(idx, n):
        if not check[i]:
            check[i] = True
            v.append(a[i])
            solve(cnt+1, i)
            v.pop()
            check[i] = False

solve(0,0)

for k in sorted(s):
    print(' '.join(map(str, k)))