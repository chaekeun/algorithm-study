from sys import stdin
input = stdin.readline

n = int(input())
p, k, m = ["" for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
ans1, ans2 = 0, 0
maxEvol = 0

def sol(idx, cnt):
    # 처음엔 재귀로 구현하려고 했으나 좀 바꿔봄
    # 알고리즘 이론에도 구현방법에서 이런 비슷한 차이가 나는게 있었는데 기억이 안남..
    while True:
        if k[idx] > m[idx]:
            break
        m[idx] = m[idx]-k[idx]+2
        cnt += 1

    return cnt 

for i in range(n):
    # 처음엔 append함수를 써서 list를 초기화하려고 했는데 그럼 함수를 너무 많이 호출하는 것 같아서 위에서 그냥 변수 선언할 때 초기화해주고 idx로 접근
    p[i] = input().strip() 
    k[i], m[i] = map(int, input().split())

for i in range(n):

    evol = sol(i, 0)
    ans1 += evol 

    if maxEvol < evol:
        maxEvol = evol
        ans2 = i

print(ans1)
print(p[ans2])
