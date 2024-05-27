from sys import stdin
input = stdin.readline

n = int(input())
cmdList = [input().strip() for _ in range(n)]
stck = []

def execCmd(cmd):
    global stck
    if cmd == 'pop':
        print(stck.pop() if len(stck)>0 else -1)
    elif cmd == 'size':
        print(len(stck))
    elif cmd == 'empty':
        print(1 if len(stck) == 0 else 0)
    elif cmd == 'top':
        print(stck[-1] if len(stck) > 0 else -1)

def execPush(num):
    global stck
    stck.append(num)

for cmd in cmdList:
    if cmd[:4] == 'push':
        execPush(int(cmd[5:]))
    else:
        execCmd(cmd)



