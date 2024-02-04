#동빈나 1이 될때까지

# #내 답안
# n, k = map(int, input().split())
# cnt = 0

# while (n!=1):
#     if n % k == 0:
#         n //=  k 
#     else:
#         n -= 1
#     cnt +=1

# print(cnt)

# #모범답안

# n, k = map(int, input().split())
# result = 0

# # 반복문 한번마다 바로 k가 나누어지는 연산이 한번 이루어지기 때문에 시간복잡도가 로그
# while True:
#     # n이 k로 나누어떨어지지 않을때 가장 가까운 나누어떨어지는 값을 찾는다.
#     target = (n // k) * k
#     # 1을 빼는 연산을 몇번할지 한 번의 연산에서 구하기 위해
#     result += (n-target)
#     n = target
#     # n이 k보다 작아서 더이상 나눌 수 없을 때 반복문 탈출
#     if n<k:
#         break
#     result += 1
#     n //= k

# result += (n-1)
# print(result)

#동빈나 상하좌우

# #모범답안
# n = int(input())
# a = [[0]*(n+1) for _ in range(n+1)]
# plans = list(map(input().split()))

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types=['L','R','U','D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]
#         nx = x+dx[i]
#         ny = x+dy[i]
#     if nx<1 or ny<1 or nx>n or ny>n:
#         continue
#     x, y = nx, ny

# print(x,y)

#동빈나 시각

# #나의 뻘짓
# n = int(input())
# time = [[(i,m) for m in range(60)],[(i,s) for s in range(60)] for i in range(n+1)]
# print(time)

# #동빈나 모범답안
# h = int(input())

# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count +=1

# print(count)

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a'))+1 

#이동할 수 있는 방향 정의
steps=[(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]

result = 0
#steps의 각 elem마다
for step in steps:
    #새로운 좌표 할당
    nr = row + step[0]
    nc = col + step[1]
    #새로운 좌표로 이동가능하면 카운트 증가
    if nr >=1 and nr<=8 and nc >=1 and nc<=8:
        result += 1

print(result)