# s1, s2 = list(map(lower(), input().split()))

# 내가 못한 것
# while True와 try except: break 문을 이용해서 예외처리
# 부분 문자열을 가지고 있는지 판단하는 방법 : t에서 몇개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는지

# while True:
#     try:
#         s, t = input().split()

#         if s.lower() in t.lower():
#             print('Yes')
#         else:
#             print('No')

#     except:
#         break

import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i == len(s):
            print('Yes')
        else:
            print('No')
    except:
        break