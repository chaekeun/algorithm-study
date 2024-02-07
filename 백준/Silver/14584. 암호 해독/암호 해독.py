from collections import deque
from sys import stdin
input = stdin.readline

str = input().strip()
n = int(input())
dict = [input().strip() for _ in range(n)]



def bfs():
    q = deque()
    q.append(0)
    check = [False for _ in range(26)]


def decode():
    
    for i in range(26):
        new_str = ""
        for k in str: # 이거 map함수를 쓸 수 있을까?
            # 새로운 string을 만들어주어야한다.
            new_str += chr((ord(k)+i-ord('a')) % 26 + ord('a'))
        for word in dict:
            if word in new_str:
                print(new_str)
                break
    
    



decode()