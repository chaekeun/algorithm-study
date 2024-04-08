from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans, minDist = 0, 200000

# # 각각의 집에 안테나를 설치해보았을 때 모든 집까지의 거리를 계산해보고 min갱신
# # 으로 하려고 했으나 시간초과..ㅎ
# for house in a:
#     sum = 0
#     # 절댓값함수 abs를 이용해서 거리를 담은 list만들고 sum함수 적용
#     sumDist = sum([abs(elem-house) for elem in a])
    
#     if sumDist < minDist:
#         ans = house
#         minDist = sumDist

# print(ans)

a.sort()
print(a[(n-1)//2])