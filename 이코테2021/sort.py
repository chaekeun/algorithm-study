from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

def solve(a, b):
    answer = 0
    for i in range(k):
        a[i], b[i] = b[i], a[i]

    answer = sum(a)
    return answer

print(solve(a,b))
    
    


