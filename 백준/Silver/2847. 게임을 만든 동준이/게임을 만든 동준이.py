from sys import stdin
input = stdin.readline

n = int(input())
a = [int(input().strip()) for _ in range(n)]
cnt = 0


# a[i+1]의 점수가 a[i]보다 작아질때까지 1만큼 감소시키는걸 반복하고
# 그 감소횟수를 count하는 함수
def reduce(idx):
    # 1. 근데 이걸 while문으로 돌릴것이냐
    # while(a[idx+1]>a[idx]):
    #     a[idx] -= 1
    #     num += 1
    # 2. 아니면 그냥 num = a[i+1]-a[i] + 1해서 a[i+1]=a[i+1]-num이랑 count = num 할것이냐
    num = a[idx+1]-a[idx]+1
    a[idx+1] -= num 
    return num

a = a[::-1]

for i in range(n-1):

    # 만약 a[i+1]이 a[i]보다 작다면:
    if a[i+1] < a[i]:
        continue
    # a[i+1]이 a[i]보다 같거나 크다면:
    # 점소감수누적횟수 += 함수실행
    cnt += reduce(i)

print(cnt)