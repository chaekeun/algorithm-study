from sys import stdin
input = stdin.readline

n = int(input().strip())
stck = []
ans = 0

def work(task):
    global ans, stck
    task[2] -= 1
    if task[2] != 0:
        stck.append(task)
    else:
        ans += task[1]

for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        if len(stck) > 0:
            temp = stck.pop()
            work(temp)
    else:
        work(cmd)

print(ans)