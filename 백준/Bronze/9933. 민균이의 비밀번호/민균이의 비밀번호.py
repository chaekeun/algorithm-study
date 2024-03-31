from sys import stdin
input = stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
pw = ''

def find():
    global pw

    for word in words:
        k = ""
        for i in range(len(word)-1, -1, -1):
            k += word[i]
        
        if k in words:
            pw = k

def solve():
    ans1 = len(pw)
    ans2 = len(pw) // 2

    print(ans1, pw[ans2])

find()
solve()