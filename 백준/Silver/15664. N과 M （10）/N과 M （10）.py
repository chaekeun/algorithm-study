n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
check = [False] * n
v = []
s = set()


def solve(cnt, idx):
    # if 정답이라면: 정답출력 or 저장 등등 
    if cnt == m: 
        s.add(tuple(v))
        return
    # for 뱉을 수 있는 모든 자식노드들에 대해서:
    for i in range(idx, n):
        # if 정답이 유망하다면:
        if not check[i]:
            # 자식노드로 이동
            check[i] = True
            v.append(a[i])
            # 재귀함수
            solve(cnt+1, i+1)
            # 부모노드로 이동 (=이전노드로 돌아간다)
            v.pop()
            check[i] = False

solve(0,0)

# sorted함수를 쓰면 코드길이가 좀 더 줄어든다
for k in sorted(s):
    print(' '.join(map(str, k)))