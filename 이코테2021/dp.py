from sys import stdin
input = stdin.readline

# # # x = int(input())

# # # d = [0]*30001

# # # for i in range(2, x+1):

# # #     #현재의 수에서 1을 빼는 경우
# # #     d[i] = d[i-1]+1

# # #     if i%2 == 0:
# # #         d[i] = mid(d[i], d[i//2]+1)
# # #     if i%3 == 0:
# # #         d[i] = mid(d[i], d[i//3]+1)
# # #     if i%5 == 0:
# # #         d[i] = mid(d[i], d[i//5]+1)

# # # print(d[x])

# # n, m = map(int, input().split())
# # array = []
# # for i in range(n):
# #     array.append(int(input()))

# # #한번 계산된 결과를 저장하기 위한 dp테이블 초기화
# # d=[10001]*(m+1)

# # d[0]=0
# # for i in range(n): #화폐단위별로 반복문 돌면서
# #     for j in range(array[i], m+1):
# #         # i-k원을 만드는 방법이 존재하는 경우
# #         if d[j-array[i]] != 10001:
# #             d[j] = min(d[j], d[j-array[i]]+1)

# # if d[m] == 10001:
# #     print(-1)
# # else:
# #     print(d[m])



# #여기서부터 나동빈 금광풀이
# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     d = []
#     index = 0
#     #이런 초기화 방식 신박
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index += m

#     for j in range(1, m):
#         for i in range(n):

#             if i == 0: left_up = 0 #예외처리
#             else: left_up = dp[i-1][j-1]
#             if i == n-1: left_down = 0
#             else: left_down = dp[i+1][j-1]
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)

#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m-1])

#     print(result)

# n = int(input())
# array = list(map(int, input().split()))
# array.reverse()

# dp = [1]*n

# for i in range(1, n):
#     for j in range(0, i):
#         if array[j]<array[i]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(n-max(dp))
